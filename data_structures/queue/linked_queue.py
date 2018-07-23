class LinkedQueue:
    """Enqueue elements at the back of the singly linked list and dequeue from the front.
    It is hard to efficiently remove elements from the tail of a singly linked list."""

    class Node:
        __slots__ = '_data', '_next'

        def __init__(self, data, next):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return
        return self._head._data

    def dequeue(self):
        if self.is_empty():
            return
        result = self._head._data
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result

    def enqueue(self, e):
        new = self.Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1
