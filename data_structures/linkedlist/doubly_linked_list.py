class DoublyLinkedList:

    class Node:
        __slots__ = '_data', '_prev', '_next'

        def __init__(self, data, prev, next):
            self._data = data
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_between(self, e, predecessor, successor):
        new = self.Node(e, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new

    def delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        pred._next = successor
        succ._prev = predecessor

        self._size -= 1
        data = node._data
        node._prev = node._next = node._data = None
        return data
