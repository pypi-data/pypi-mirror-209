import functools
import typing

from sparta.memcached.base import SpartaCache


class SpartaCacheIgnoreErrorsDecorator(SpartaCache):
    """
    Decorates the behaviour of an existing SpartaCache.
    """

    def __init__(
        self,
        delegate: SpartaCache,
    ):
        super().__init__()
        self.delegate = delegate

    def __repr__(self):
        return repr(self.delegate)

    def __str__(self):
        return str(self.delegate)

    def __getitem__(self, key):
        return self.delegate.__getitem__(key)

    def __setitem__(self, key, value):
        return self.delegate.__setitem__(key, value)

    def __delitem__(self, key):
        return self.delegate.__delitem__(key)

    def __contains__(self, key):
        return self.delegate.__contains__(key)

    def map_key(self, key) -> str:
        return self.delegate.map_key(key)

    def add(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.add, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def append(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.append, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def cas(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.cas, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def decr(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.decr, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def delete(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.delete, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def get(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.get, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def gets(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.gets, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def incr(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.incr, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def prepend(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.prepend, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def replace(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.replace, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def set(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.set, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def touch(self, key, *args, ignore_errors: bool = True, **kwargs):
        func = functools.partial(self.delegate.touch, key, *args, **kwargs)
        return self._call_func_and_handle_errors(func, ignore_errors)

    def _call_func_and_handle_errors(self, func: typing.Callable, ignore_errors: bool):
        try:
            return func()
        except Exception as e:
            if ignore_errors:
                self.logger.warning(e)
            else:
                raise e
