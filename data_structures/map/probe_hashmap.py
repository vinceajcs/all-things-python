class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""

    _AVAIL = object()

    def _is_available(self, j):
        return self._map[j] is None or self._map[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._map[j] is None:
                    return (False, firstAvail)
                elif k == self._map[j]._key:
                    return (True, j)
                j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: %s' % repr(k))
        return self._map[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._map[s] = self.Item(k, v)
            self._n += 1
        else:
            self._map[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: %s' % repr(k))
        self._map[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._map)):
            if not self._is_available(j):
                yield self._map[j]._key
