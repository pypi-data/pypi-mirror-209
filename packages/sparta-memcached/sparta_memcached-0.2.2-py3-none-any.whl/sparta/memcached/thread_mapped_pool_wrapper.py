import pylibmc

from sparta.memcached.base import SpartaCache


class SpartaCacheThreadMappedPoolWrapper(SpartaCache):
    """
    Wrapper around pylibmc.ThreadMappedPool to support key_prefix.
    Also see https://github.com/memcached/memcached/wiki/Commands.
    """

    def __init__(
        self,
        pool: pylibmc.ThreadMappedPool,
        key_prefix: str,
    ):
        super().__init__()
        self.pool = pool
        self.key_prefix = key_prefix if isinstance(key_prefix, str) else str(key_prefix)

    def map_key(self, key) -> str:
        return self.key_prefix + key if self.key_prefix else key

    def __repr__(self):
        return "<%s for %s>" % (self.__class__.__name__, self.pool)

    def __str__(self):
        return "<%s for %s>" % (self.__class__.__name__, self.pool)

    def __getitem__(self, key):
        with self.pool.reserve() as client:
            return client.__getitem__(self.map_key(key))

    def __setitem__(self, key, value):
        with self.pool.reserve() as client:
            return client.__setitem__(self.map_key(key), value)

    def __delitem__(self, key):
        with self.pool.reserve() as client:
            return client.__delitem__(self.map_key(key))

    def __contains__(self, key):
        with self.pool.reserve() as client:
            return client.__contains__(self.map_key(key))

    def add(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.add(self.map_key(key), *args, **kwargs)

    def append(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.append(self.map_key(key), *args, **kwargs)

    def cas(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.cas(self.map_key(key), *args, **kwargs)

    def decr(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.decr(self.map_key(key), *args, **kwargs)

    def delete(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.delete(self.map_key(key), *args, **kwargs)

    def get(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.get(self.map_key(key), *args, **kwargs)

    def gets(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.gets(self.map_key(key), *args, **kwargs)

    def incr(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.incr(self.map_key(key), *args, **kwargs)

    def prepend(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.prepend(self.map_key(key), *args, **kwargs)

    def replace(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.replace(self.map_key(key), *args, **kwargs)

    def set(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.set(self.map_key(key), *args, **kwargs)

    def touch(self, key, *args, **kwargs):
        with self.pool.reserve() as client:
            return client.touch(self.map_key(key), *args, **kwargs)
