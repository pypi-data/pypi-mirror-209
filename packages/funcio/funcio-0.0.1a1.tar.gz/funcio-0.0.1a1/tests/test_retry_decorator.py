import time
from typing import Callable, Any

import pytest

from funcio import retry


def create_test_func(fail_count: int = 1,
                     fail_exception: Exception = Exception(),
                     execution_time: float = 0.0,
                     return_value: Any = None) -> Callable:

    def foo():
        nonlocal fail_count, fail_exception, execution_time, return_value
        time.sleep(execution_time)
        if fail_count > 0:
            fail_count -= 1
            raise fail_exception
        return return_value

    return foo


@pytest.mark.parametrize('fail_count', [0, 1, 2, 3])
def test_retry(fail_count: int):

    foo = create_test_func(fail_count=fail_count)
    foo = retry(foo)
    foo()


@pytest.mark.parametrize('fail_count', [1, 2, 3])
def test_raise_exception(fail_count: int):
    foo = create_test_func(fail_count=fail_count, fail_exception=ValueError())
    foo = retry(tries=fail_count - 1)(foo)

    with pytest.raises(ValueError):
        foo()


@pytest.mark.parametrize('tries', [0, 1, 2, 3])
def test_retry_tries_number(tries: int):

    foo = create_test_func(fail_count=tries)
    foo = retry(tries=tries)(foo)
    foo()


@pytest.mark.parametrize('timeout', [0.0, 0.5, 1.0, 1.5])
@pytest.mark.parametrize('execution_time', [0.1])
def test_retry_timeout(timeout: float, execution_time: float, overhead: float = 0.01):

    foo = create_test_func(fail_count=99, execution_time=execution_time)
    foo = retry(timeout=timeout)(foo)

    with pytest.raises(Exception):
        start = time.perf_counter()
        foo()
    elapsed = time.perf_counter() - start

    assert timeout <= elapsed <= timeout + execution_time + overhead


@pytest.mark.parametrize('delay', [0.0, 0.5, 1.0])
@pytest.mark.parametrize('fail_count', [0, 1, 2, 3])
@pytest.mark.parametrize('execution_time', [0.0, 0.1])
def test_retry_delay(delay: float, fail_count: int, execution_time: float, overhead: float = 0.01):

    foo = create_test_func(fail_count=fail_count, execution_time=execution_time)
    foo = retry(delay=delay)(foo)

    start = time.perf_counter()
    foo()
    elapsed = time.perf_counter() - start

    estimated_runtime = execution_time * (fail_count + 1) + delay * fail_count

    assert estimated_runtime <= elapsed <= estimated_runtime + overhead


def test_retry_with_exception():
    foo = create_test_func(fail_count=1, fail_exception=ValueError())
    foo = retry(exceptions=(ValueError,))(foo)

    foo()

    bar = create_test_func(fail_count=1, fail_exception=KeyError())
    bar = retry(tries=1, exceptions=(ValueError,))(bar)

    with pytest.raises(KeyError):
        bar()

