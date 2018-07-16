class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def add_first(self, item):
        if self.length == 0:
            self.head = Node(item)
            self.length += 1
        else:
            node = Node(item)
            node.next = self.head
            self.head = node
            self.length += 1
