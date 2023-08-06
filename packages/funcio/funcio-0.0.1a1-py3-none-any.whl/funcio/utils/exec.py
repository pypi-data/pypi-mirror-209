import ast
import inspect
from collections.abc import MutableMapping
from types import FrameType, CodeType
from typing import Iterator
import ctypes


class FrameLocals(MutableMapping):
    def __init__(self, frame: FrameType):
        self._frame = frame

    def __getitem__(self, key):
        return self._frame.f_locals[key]

    def __setitem__(self, key, value):
        self._frame.f_locals[key] = value
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(self._frame), ctypes.c_int(0))

    def __delitem__(self, key):
        del self._frame.f_locals[key]
        ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(self._frame), ctypes.c_int(1))

    def __len__(self) -> int:
        return len(self._frame.f_locals)

    def __iter__(self) -> Iterator:
        return iter(self._frame.f_locals)


def exec_in_frame(source: str | bytes | CodeType, frame: FrameType):
    """
    Execute code in frame with globals and locals updated
    """
    frame_locals = None
    if frame.f_globals is not frame.f_locals:
        frame_locals = FrameLocals(frame)

    exec(source, frame.f_globals, frame_locals)


async def async_exec_in_frame(source: str | bytes | CodeType, frame: FrameType):
    """
    Execute async code in frame with globals and locals updated
    """
    if isinstance(source, (str, bytes)):
        source = compile(source, filename='<string>', mode='exec', flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    frame_locals = None
    if frame.f_globals is not frame.f_locals:
        frame_locals = FrameLocals(frame)

    result = eval(source, frame.f_globals, frame_locals)
    if inspect.iscoroutine(result) and result.cr_code is source:
        await result

