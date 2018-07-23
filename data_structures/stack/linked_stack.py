class LinkedStack:

    class Node:
        __slots__ = '_data', '_next'

        def __init__(self, data, next):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self.Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            return
        return self._head._data

    def pop(self):
        if self.is_empty():
            return
        result = self._head._data
        self._head = self._head._next
        self._size -= 1
        return result
