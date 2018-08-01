from map_base import MapBase


class UnsortedMap(MapBase):

    def __init__(self):
        self._map = []

    def __getitem__(self, k):
        for item in self._map:
            if k == item._key:
                return item._value

        raise KeyError('Key Error: %s' % repr(k))

    def __setitem__(self, k, v):
        for item in self._map:
            if k == item._key:
                item._value = v
                return

        self._map.append(self.Item(k, v))

    def __delitem__(self, k):
        for i in range(len(self._map)):
            if k == self._map[i]._key:
                self._map.pop(i)
                return

        raise KeyError('Key Error: %s' % repr(k))

    def __len__(self):
        return len(self._map)

    def __iter__(self):
        for item in self._map:
            yield item._key
