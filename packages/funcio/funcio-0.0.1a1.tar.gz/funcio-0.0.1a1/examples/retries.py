import ast
import time
from types import CodeType, FrameType
from typing import Callable, Literal, Awaitable
import inspect
from textwrap import dedent, indent
import ctypes


def retry(tries: int = None):
    return Retry(tries)


class Retry:
    def __init__(self, tries: int = None):
        if tries is not None and tries < 0:
            raise ValueError('tries must be greater than or equal to 0')
        self.tries = tries

        self._frame = None

    def __call__(self, func: Callable):

        def wrapper(*args, **kwargs):
            tries = self.tries
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tries is None:
                        print(f'Exception "{e.__class__.__name__}: {e}" occurred, retrying...')
                        continue

                    tries -= 1
                    if tries <= 0:
                        raise e

                    print(f'Exception "{e.__class__.__name__}: {e}" occurred, retrying...')

        return wrapper

    def __enter__(self):
        self._frame = inspect.currentframe().f_back
        return self

    async def __aenter__(self):
        self._frame = inspect.currentframe().f_back
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None or self._frame is None:
            return False

        print(f'Exception "{exc_type.__name__}: {exc_val}" occurred, retrying...')

        compiled = get_with_source(self._frame, self._frame.f_lineno, 'compiled')
        # retry context
        tries = self.tries
        while True:
            try:
                exec_in_frame(compiled, self._frame)
                return True
            except Exception as e:
                if tries is None:
                    print(f'Exception "{e.__class__.__name__}: {e}" occurred, retrying...')
                    continue

                tries -= 1
                if tries <= 0:
                    raise e

                print(f'Exception "{e.__class__.__name__}: {e}" occurred, retrying...')

        return False

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None or self._frame is None:
            return False

        print(f'Exception "{exc_type.__name__}: {exc_val}" occurred, retrying...')

        with_source = get_with_source(self._frame, self._frame.f_lineno, 'text')
        # retry context
        tries = self.tries
        while True:
            try:
                await async_exec_in_frame(with_source, self._frame)
                return True
            except Exception as e:
                if tries is None:
                    print(f'Exception "{e.__class__.__name__}: {e}" occurred, retrying...')
                    continue

                tries -= 1
                if tries <= 0:
                    raise e

                print(f'Exception "{e.__class__.__name__}: {e}" occurred, retrying...')

        return False


def in_context_walk(node: ast.AST):
    from collections import deque
    todo = deque([node])
    while todo:
        node = todo.popleft()
        todo.extend(
            filter(lambda n: not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Module)),
                   ast.iter_child_nodes(node))
        )
        yield node


def get_with_source(frame: FrameType, with_lineno: int, output: Literal['text', 'compiled', 'ast']) -> str | bytes | ast.AST:
    # get frame source code
    source_lines, start_lineno = inspect.getsourcelines(frame)
    source = ''.join(source_lines)
    source = dedent(source)
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
               in_context_walk(node))
    )
    with_node = next(filter(lambda n: isinstance(n, (ast.With, ast.AsyncWith)) and n.lineno == with_lineno, ast.walk(node)))
    with_body = ast.Module(body=global_nodes + with_node.body, type_ignores=[])

    match output:
        case 'text':
            return ast.unparse(with_body)
        case 'compiled':
            return compile(with_body, filename='<ast>', mode='exec')
        case 'ast':
            return with_body
        case _:
            raise ValueError('output must be one of "text", "compiled", or "ast"')


def exec_in_frame(source: str | bytes | CodeType, frame: FrameType):
    """
    Execute code in frame with globals and locals updated
    """
    frame_locals = None
    frame_locals_keys = []
    if frame.f_globals is not frame.f_locals:
        frame_locals = frame.f_locals.copy()
        frame_locals_keys = list(frame_locals.keys())

    try:
        exec(source, frame.f_globals, frame_locals)
    finally:
        if frame.f_globals is not frame.f_locals:
            frame.f_locals.update(frame_locals)
            removed_keys = set(frame_locals_keys) - set(frame_locals.keys())
            for key in removed_keys:
                frame.f_locals.pop(key, None)
            ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(1))


async def async_exec_in_frame(source: str, frame: FrameType):
    wrapped = f'''
import asyncio
import inspect
# print(f'locals: {{locals()}}')
# print(f'globals: {{globals()}}')
async def __async_wrapper__(__frame):
    import inspect
    import ctypes
    __inner_frame = inspect.currentframe()
    __inner_frame.f_locals.update(__frame.f_locals)
    ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(__inner_frame), ctypes.c_int(1))
    # print(f'locals: {{locals()}}')
    # print(f'__frame.f_locals: {{__frame.f_locals}}')
    try:
{indent(source, ' '*8)}
    finally:
        __frame.f_locals.update(__inner_frame.f_locals)
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(__frame), ctypes.c_int(1))
__wrapper_task = asyncio.get_event_loop().create_task(__async_wrapper__(inspect.currentframe()))
    '''
    wrapped = dedent(wrapped)
    compiled = compile(wrapped, filename='<ast>', mode='exec')

    frame_locals = frame.f_globals
    frame_locals_keys = []
    if frame.f_globals is not frame.f_locals:
        frame_locals = frame.f_locals.copy()
        frame_locals_keys = list(frame_locals.keys())

    try:
        exec(compiled, frame.f_globals, frame_locals)
        await frame_locals['__wrapper_task']
    finally:
        if frame.f_globals is not frame.f_locals:
            frame.f_locals.update(frame_locals)
            removed_keys = set(frame_locals_keys) - set(frame_locals.keys())
            for key in removed_keys:
                frame.f_locals.pop(key, None)
            ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(frame), ctypes.c_int(1))


if __name__ == '__main__':
    # retry decorator

    # @retry(3)
    # def function():
    #     print('test retry decorator')
    #     time.sleep(0.5)
    #     raise Exception('test exception')
    #
    # function()

    # retry context

    # with retry(3):
    #     print('test retry context')
    #     time.sleep(0.5)
    #     raise Exception('test exception')
    #
    # print('test retry context')

    from textwrap import dedent

    def func():
        abc = 5
        s = '''
            123
    456
        '''
        print(s)

    source = inspect.getsource(func)
    source = dedent(source)

    print('vvvvvvv')
    print(source)
    print('^^^^^^^')
    print('vvvvvvv output 1')
    func()
    print('^^^^^^^')
    exec(source)
    print('vvvvvvv output 2')
    locals()['func']()
    print('^^^^^^^')


