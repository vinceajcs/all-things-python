class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)

    def peek(self):
        return self._items[len(self._items) - 1]
