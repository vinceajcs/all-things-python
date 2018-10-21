"""Using a dict + deque."""


class LRUCache:
    def __init__(self, capacity):
        self.deque = collections.deque()
        self.lookup = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.lookup:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.lookup[key]

    def put(self, key, value):
        if key in self.lookup:
            self.deque.remove(key)
        elif len(self.lookup) == self.capacity:
            lru = self.deque.popleft()  # remove the LRU element
            del self.lookup[lru]

        self.deque.append(key)
        self.lookup[key] = value


"""Using a dict + doubly LL. We insert from at the tail of the LL and remove from the head."""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lookup = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.lookup:
            return -1
        n = self.lookup[key]
        self._remove(n)
        self._add(n)
        return n.value

    def put(self, key, value):
        if key in self.lookup:
            self._remove(self.lookup[key])
        elif len(self.lookup) == self.capacity:
            lru = self.head.next.key
            self._remove(self.head.next)  # remove the LRU element
            del self.lookup[lru]

        n = Node(key, value)
        self.lookup[key] = n
        self._add(n)

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
