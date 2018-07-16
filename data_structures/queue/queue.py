class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, data):
        node = Node(data)
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        node = self.head.data
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.last = None
        return node
