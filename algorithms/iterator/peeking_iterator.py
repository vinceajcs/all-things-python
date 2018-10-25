"""Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that supports the peek() operation."""


class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.done = False
        self.next_element = None
        self.advance_iter()

    def peek(self):
        return self.next_element

    def next(self):
        result = self.next_element
        self.advance_iter()
        return result

    def has_next(self):
        return not self.done

    # private method
    def advance_iter(self):
        if self.iter.has_next():
            self.next_element = self.iter.next()
        else:
            self.done = True
