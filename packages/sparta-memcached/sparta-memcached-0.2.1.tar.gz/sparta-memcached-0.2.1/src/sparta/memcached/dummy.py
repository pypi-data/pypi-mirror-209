from sparta.memcached.base import SpartaCache


class SpartaCacheDummy(SpartaCache):
    """
    Dummy implementation, useful to disable caching without breaking code deps.
    """

    def map_key(self, key) -> str:
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, key):
        pass

    def atomic_append(self, key, value, _retries=3, *args, **kwargs):
        pass

    def add(self, key, *args, **kwargs):
        pass

    def append(self, key, *args, **kwargs):
        pass

    def cas(self, key, *args, **kwargs):
        pass

    def decr(self, key, *args, **kwargs):
        pass

    def delete(self, key, *args, **kwargs):
        pass

    def get(self, key, *args, **kwargs):
        pass

    def gets(self, key, *args, **kwargs):
        pass

    def incr(self, key, *args, **kwargs):
        pass

    def prepend(self, key, *args, **kwargs):
        pass

    def replace(self, key, *args, **kwargs):
        pass

    def set(self, key, *args, **kwargs):
        pass

    def touch(self, key, *args, **kwargs):
        pass
