class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence
        self._i = -1  # will incremenet to 0 on frist call to next

    def __next__(self):
        """Return the next element, or raise StopIteraton error."""
        self._i += 1
        if self._i < len(self._seq):
            return(self._seq[self._i])
        else:
            raise StopIteration()

    def __iter__(self):
        """Iterator returns itself as an iterator."""
        return self
