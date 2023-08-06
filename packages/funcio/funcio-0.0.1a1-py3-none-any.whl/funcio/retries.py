import ast
import asyncio
import functools
import inspect
import itertools
import random
import time
from collections.abc import Iterable
from dataclasses import dataclass
from types import FrameType
from typing import overload, Callable, Any, Type, Iterator, Literal
import textwrap

from .utils.exec import exec_in_frame, async_exec_in_frame
from .utils.parameters import EMPTY


@dataclass(frozen=True, slots=True)
class FunctionSignature:
    func: Callable
    args: tuple[Any, ...]
    kwargs: dict[str, Any]


@dataclass(frozen=True, slots=True)
class FunctionResult:
    return_value: Any = None
    exception: Exception = None

    @property
    def is_success(self) -> bool:
        return self.exception is None

    @property
    def is_failure(self) -> bool:
        return self.exception is not None

    def result(self) -> Any:
        if self.exception is not None:
            raise self.exception
        return self.return_value


@dataclass(frozen=True, slots=True)
class RetryParams:
    tries: int = None
    timeout: float = None
    delay: float | Iterable[float | None] = None
    backoff: bool | float = False
    jitter: bool | float = False
    exceptions: tuple[Type[Exception], ...] = (Exception,)
    return_values: tuple[Any, ...] = EMPTY


@dataclass(slots=True)
class RetryState:
    tried: int
    start_time: float
    delayed: float


@dataclass(frozen=True, slots=True)
class RetryContext:
    signature: FunctionSignature
    result: FunctionResult
    params: RetryParams
    state: RetryState


@overload
def retry(
        func: Callable[..., Any] = None,
        /,
        tries: int = None,
        timeout: float = None,
        delay: float | Iterable[float | None] = None,
        backoff: bool | float = False,
        jitter: bool | float = False,
        exceptions: tuple[Type[Exception], ...] = (Exception,),
        return_values: tuple[Any, ...] = EMPTY,
) -> Callable[..., Any]:
    ...


@overload
def retry(
        tries: int = None,
        timeout: float = None,
        delay: float | Iterable[float | None] = None,
        backoff: bool | float = False,
        jitter: bool | float = False,
        exceptions: tuple[Type[Exception], ...] = (Exception,),
        return_values: tuple[Any, ...] = EMPTY,
) -> Callable[..., Any]:
    ...


def retry(
        func: Callable[..., Any] | int = None,
        /,
        tries: int = None,
        timeout: float = None,
        delay: float | Iterable[float | None] = None,
        backoff: bool | float = False,
        jitter: bool | float = False,
        exceptions: tuple[Type[Exception], ...] = (Exception,),
        return_values: tuple[Any, ...] = EMPTY,
) -> 'Retry' | Callable[..., Any]:
    if isinstance(func, int):
        if tries is not None:
            raise TypeError("retry() got multiple values for argument 'tries'")
        tries = func
        func = None

    f = Retry(tries, timeout, delay, backoff, jitter, exceptions, return_values)
    if func is not None:
        return f(func)
    return f


class Retry:
    def __init__(self,
                 tries: int = None,
                 timeout: float = None,
                 delay: float | Iterable[float | None] = None,
                 backoff: bool | float = False,
                 jitter: bool | float = False,
                 exceptions: tuple[Type[Exception], ...] = (Exception,),
                 return_values: tuple[Any, ...] = EMPTY,
                 ):
        self.tries = tries
        self.timeout = timeout
        self.delay = delay
        self.backoff = backoff
        self.jitter = jitter
        self.exceptions = exceptions
        self.return_values = return_values

        self._frame = None

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        if not callable(func):
            raise TypeError('func must be a callable')

        params = RetryParams(
            tries=self.tries,
            timeout=self.timeout,
            delay=self.delay,
            backoff=self.backoff,
            jitter=self.jitter,
            exceptions=self.exceptions,
            return_values=self.return_values,
        )

        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                signature = FunctionSignature(func, args, kwargs)
                result = await self._async_run(signature)
                return await self._async_maybe_retry(signature, result, params)
        else:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                signature = FunctionSignature(func, args, kwargs)
                result = self._run(signature)
                return self._maybe_retry(signature, result, params)

        return wrapper

    def __enter__(self):
        self._frame = inspect.currentframe().f_back

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None or self._frame is None:
            return False

        result = FunctionResult(exception=exc_val)
        params = RetryParams(
            tries=self.tries,
            timeout=self.timeout,
            delay=self.delay,
            backoff=self.backoff,
            jitter=self.jitter,
            exceptions=self.exceptions,
            return_values=self.return_values,
        )
        state = RetryState(
            tried=0,
            start_time=time.time(),
            delayed=0,
        )
        if self._needs_retry(result, params, state):
            compiled = _extract_with_context_source(self._frame, self._frame.f_lineno, 'compiled')
            signature = FunctionSignature(
                func=exec_in_frame,
                args=(compiled, self._frame),
                kwargs={},
            )
            self._retry(signature, result, params, state)
            return True

        return False

    async def __aenter__(self):
        self._frame = inspect.currentframe().f_back

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None or self._frame is None:
            return False

        result = FunctionResult(exception=exc_val)
        params = RetryParams(
            tries=self.tries,
            timeout=self.timeout,
            delay=self.delay,
            backoff=self.backoff,
            jitter=self.jitter,
            exceptions=self.exceptions,
            return_values=self.return_values,
        )
        state = RetryState(
            tried=0,
            start_time=time.time(),
            delayed=0,
        )
        if self._needs_retry(result, params, state):
            compiled = _extract_with_context_source(self._frame, self._frame.f_lineno, 'compiled', async_with=True)
            signature = FunctionSignature(
                func=async_exec_in_frame,
                args=(compiled, self._frame),
                kwargs={},
            )
            await self._async_retry(signature, result, params, state)
            return True

        return False

    def _run(self, signature: FunctionSignature) -> FunctionResult:
        try:
            ret = signature.func(*signature.args, **signature.kwargs)
        except Exception as e:
            return FunctionResult(exception=e)
        else:
            return FunctionResult(return_value=ret)

    async def _async_run(self, signature: FunctionSignature) -> FunctionResult:
        try:
            ret = await signature.func(*signature.args, **signature.kwargs)
        except Exception as e:
            return FunctionResult(exception=e)
        else:
            return FunctionResult(return_value=ret)

    def _needs_retry(self,
                     # signature: FunctionSignature,
                     result: FunctionResult,
                     params: RetryParams,
                     state: RetryState) -> bool:

        need_retry = False

        if result.is_failure:
            if any(isinstance(result.exception, e) for e in params.exceptions):
                need_retry = True
        else:
            if params.return_values is not EMPTY and result.return_value in params.return_values:
                need_retry = True

        if need_retry:
            if (
                    (params.tries is None or params.tries - state.tried > 0) and
                    (params.timeout is None or time.time() - state.start_time < params.timeout)
            ):
                return True

        return False

    def _maybe_retry(self,
                     signature: FunctionSignature,
                     result: FunctionResult,
                     params: RetryParams,
                     ) -> Any:
        state = RetryState(
            tried=0,
            start_time=time.time(),
            delayed=0,
        )
        if self._needs_retry(result, params, state):
            return self._retry(signature, result, params, state)

        return result.result()

    async def _async_maybe_retry(self,
                                 signature: FunctionSignature,
                                 result: FunctionResult,
                                 params: RetryParams,
                                 ) -> Any:
        state = RetryState(
            tried=0,
            start_time=time.time(),
            delayed=0,
        )
        if self._needs_retry(result, params, state):
            return await self._async_retry(signature, result, params, state)

        return result.result()

    def _retry(self,
               signature: FunctionSignature,
               result: FunctionResult,
               params: RetryParams,
               state: RetryState) -> Any:

        delay_iter = _get_delay_iter(params.delay, params.backoff, params.jitter)

        while True:
            # delay
            state.delayed = next(delay_iter)
            if state.delayed is not None:
                time.sleep(state.delayed)

            # run function
            result = self._run(signature)

            # update state
            state.tried += 1

            # check if it needs retry
            if self._needs_retry(result, params, state):
                continue

            # return result
            return result.result()

    async def _async_retry(self,
                           signature: FunctionSignature,
                           result: FunctionResult,
                           params: RetryParams,
                           state: RetryState) -> Any:

        delay_iter = _get_delay_iter(params.delay, params.backoff, params.jitter)

        while True:
            # delay
            state.delayed = next(delay_iter)
            if state.delayed is not None:
                await asyncio.sleep(state.delayed)

            # run function
            result = await self._async_run(signature)

            # update state
            state.tried += 1

            # check if it needs retry
            if self._needs_retry(result, params, state):
                continue

            # return result
            return result.result()


def _get_delay_iter(delay: float | Iterable[float],
                    backoff: bool | float,
                    jitter: bool | float) -> Iterator[float | None]:
    if delay is None or isinstance(delay, (int, float)):
        delay_iter = itertools.repeat(delay)
    else:
        delay_iter = iter(delay)

    if backoff:
        raise NotImplementedError('backoff is not implemented yet')

    delay_item = EMPTY
    delay_value = None
    while True:
        delay_item = next(delay_iter, delay_item)
        if delay_item is EMPTY:
            raise ValueError('got an empty delay iterator')
        elif delay_item is None:
            yield None

        delay_value = delay_item
        if isinstance(jitter, bool) and jitter:
            delay_value *= random.uniform(0, 1)

        yield delay_value


def _ast_walk_local(node: ast.AST):
    from collections import deque
    todo = deque([node])
    while todo:
        node = todo.popleft()
        todo.extend(
            filter(lambda n: not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)),
                   ast.iter_child_nodes(node))
        )
        yield node


def _extract_with_context_source(frame: FrameType,
                                 with_lineno: int,
                                 output: Literal['text', 'compiled', 'ast'],
                                 async_with: bool = False) -> str | bytes | ast.AST:
    # get frame source code
    source_lines, start_lineno = inspect.getsourcelines(frame)
    source = ''.join(source_lines)
    source = textwrap.dedent(source)
    if start_lineno != 0:
        with_lineno -= start_lineno - 1
    # parse source code
    node = ast.parse(source)
    # remove function or class definition if it is the only statement in the code block
    if len(node.body) == 1 and isinstance(node.body[0], (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        node = node.body[0]
    # get all global nodes in the same code block and before with statement
    global_nodes = list(
        filter(lambda n: isinstance(n, ast.Global) and n.lineno < with_lineno,
               _ast_walk_local(node))
    )
    # find with statement
    with_type = ast.AsyncWith if async_with else ast.With
    with_node = next(
        filter(lambda n: isinstance(n, with_type) and n.lineno == with_lineno, ast.walk(node)))
    # extract with body
    with_body = ast.Module(body=global_nodes + with_node.body, type_ignores=[])

    # convert to output format
    match output:
        case 'text':
            return ast.unparse(with_body)  # type: ignore
        case 'compiled':
            return compile(with_body, frame.f_code.co_filename, 'exec',
                           flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT if async_with else 0)  # type: ignore
        case 'ast':
            return with_body  # type: ignore
        case _:
            raise ValueError('output must be one of "text", "compiled", or "ast"')
