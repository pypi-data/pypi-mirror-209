import sys

from abc import ABCMeta
from functools import wraps

from PySide6.QtCore import QObject, QThread


class CaseInsensitiveDict(dict):
    @classmethod
    def _k(cls, key):
        return key.lower() if isinstance(key, str) else key

    def __init__(self, *args, **kwargs):
        super(CaseInsensitiveDict, self).__init__(*args, **kwargs)
        self._convert_keys()
    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(self.__class__._k(key))
    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(self.__class__._k(key), value)
    def __delitem__(self, key):
        return super(CaseInsensitiveDict, self).__delitem__(self.__class__._k(key))
    def __contains__(self, key):
        return super(CaseInsensitiveDict, self).__contains__(self.__class__._k(key))
    def has_key(self, key):
        return super(CaseInsensitiveDict, self).has_key(self.__class__._k(key))
    def pop(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).pop(self.__class__._k(key), *args, **kwargs)
    def get(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).get(self.__class__._k(key), *args, **kwargs)
    def setdefault(self, key, *args, **kwargs):
        return super(CaseInsensitiveDict, self).setdefault(self.__class__._k(key), *args, **kwargs)
    def update(self, E=None, **F):
        super(CaseInsensitiveDict, self).update(self.__class__(E))
        super(CaseInsensitiveDict, self).update(self.__class__(**F))
    def _convert_keys(self):
        for k in list(self.keys()):
            v = super(CaseInsensitiveDict, self).pop(k)
            self.__setitem__(k, v)


class SingletonType(type(QObject)):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


def synchronized(lock):
    """ Synchronization decorator. """
    def wrap(f):
        def newFunction(*args, **kw):
            lock_ = args[0].lock if lock is None else lock
            lock_.lock()
            try:
                return f(*args, **kw)
            finally:
                lock_.unlock()
        return newFunction
    return wrap


def export(f):
    @wraps(f)
    def exported_function(*args, **kwargs):
        return f(*args, **kwargs)
    return exported_function


def export_runtime(f):
    from sknrf.model.runtime import RuntimeThread

    @wraps(f)
    def exported_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception:
            thread = RuntimeThread.currentThread()
            exception_info = sys.exc_info()
            try:
                thread.error.emit(*exception_info)       # RuntimeThread running in Graphical Mode
            except AttributeError:
                raise exception_info[1]                  # MainThread running in Non-Graphical Mode
            thread.exec_()
    return exported_function
