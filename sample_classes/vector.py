class Vector:

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, i):
        """Return ith coordinate of vector."""
        return self._coords[i]

    def __setitem(self, i, val):
        """Set ith coordinate of vector to given value."""
        self.coords[i] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('Dimensions must be the same')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differes from other."""
        return not self == other  # rely on existing __eq__ def

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


v = Vector(5)
print(v)
