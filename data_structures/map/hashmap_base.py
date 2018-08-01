from map_base import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hashtable using MAD compression."""

    def __init__(self, cap=11, p=109345121):
        self._map = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._scale) % self._prime % len(self._map)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._map) // 2:
            self._resize(2 * len(self._map) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def resize(self, c):
        old = list(self.items())
        self._map = c * [None]
        self.n = 0
        for (key, value) in old:
            self[key] = value
