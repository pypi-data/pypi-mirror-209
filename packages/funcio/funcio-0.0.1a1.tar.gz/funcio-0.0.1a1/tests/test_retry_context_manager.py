import time

import pytest

from funcio import retry


def test_retry():
    first = True
    with retry():
        if first:
            first = False
            raise ValueError('test')


def test_raise_exception():
    with pytest.raises(ValueError):
        with retry(1):
            raise ValueError('test')


@pytest.mark.asyncio
async def test_await_syntax_error():
    async def foo():
        return True

    with pytest.raises(SyntaxError):
        first = True
        with retry(1):
            if first:
                first = False
                raise ValueError('test')
            await foo()


def test_create_local_variable():
    first = True
    with retry(1):
        if first:
            first = False
            raise ValueError('test')
        flag = True

    assert flag is True


def test_update_local_variable():
    first = True
    flag = False
    with retry(1):
        if first:
            first = False
            raise ValueError('test')
        flag = True

    assert flag is True


def test_remove_local_variable():
    first = True
    flag = True
    with retry(1):
        if first:
            first = False
            raise ValueError('test')
        del flag

    assert 'flag' not in locals()


def test_retry_tries_numer(tries: int = 3):
    first = True
    count = 0
    with retry(tries=tries):
        if first:
            first = False
            raise ValueError('test')

        count += 1
        if count < tries:
            raise ValueError('test')

    assert count == tries


def test_retry_timeout(timeout: float = 1.0):

    with pytest.raises(ValueError):
        start = time.perf_counter()
        with retry(timeout=timeout):
            time.sleep(0.5)
            raise ValueError('test')
    elapsed = time.perf_counter() - start

    assert elapsed >= timeout



