# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import queue
import time
import types


from functools import wraps
from threading import Thread as BasicThread


def __dir__():
    return (
            'Thread',
            'launch',
            'threaded'
           )


__all__ = __dir__()


class Thread(BasicThread):

    def __init__(self, func, thrname, *args, daemon=True):
        super().__init__(None, self.run, thrname, (), {}, daemon=daemon)
        self._result = None
        self.name = thrname or name(func)
        self.queue = queue.Queue()
        self.queue.put_nowait((func, args))
        self.sleep = None
        self.starttime = time.time()

    def __iter__(self):
        return self

    def __next__(self):
        for k in dir(self):
            yield k

    def join(self, timeout=None):
        super().join(timeout)
        return self._result

    def run(self):
        func, args = self.queue.get()
        self._result = func(*args)


def launch(func, *args, **kwargs):
    thrname = kwargs.get('name', '')
    thr = Thread(func, thrname, *args)
    thr.start()
    return thr


def name(obj):
    typ = type(obj)
    if isinstance(typ, types.ModuleType):
        return obj.__name__
    if '__self__' in dir(obj):
        return '%s.%s' % (obj.__self__.__class__.__name__, obj.__name__)
    if '__class__' in dir(obj) and '__name__' in dir(obj):
        return '%s.%s' % (obj.__class__.__name__, obj.__name__)
    if '__class__' in dir(obj):
        return obj.__class__.__name__
    if '__name__' in dir(obj):
        return '%s.%s' % (obj.__class__.__name__, obj.__name__)
    return None


def threaded(func, *args, **kwargs):

    @wraps(func)
    def threadedfunc(*args, **kwargs):
        thr = launch(func, *args, **kwargs)
        if args:
            args[0].__thr__ = thr
        return thr

    return threadedfunc
