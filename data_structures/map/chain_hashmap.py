from hashmap_base import HashMapBase


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._map[j]
        if bucket is None:
            raise KeyError('Key Error: %s' % repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._map[j] is None:
            self._map[j] = UnsortedMap()
        oldsize = len(self._map[j])
        self._map[j][k] = v
        if len(self._map[j]) > oldsize:  # if key did not previously exist
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._map[j]
        if bucket is None:
            raise KeyError('Key Error: %s' % repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._map:
            if bucket is not None:
                for key in bucket:
                    yield key
