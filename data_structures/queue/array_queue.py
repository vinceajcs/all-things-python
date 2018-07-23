class ArrayQueue:
    """Uses a circular array to implement the queue ADT. This avoids using pop(0)."""
    CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._data[self._front]

    def dequeue(self):
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        new_index = (self._front + self._size) % len(self._data)
        self._data[new_index] = e
        self._size += 1

    def resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
