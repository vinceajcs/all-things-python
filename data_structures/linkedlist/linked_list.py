"""Implementation of singly linked list."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_first(self, item):
        if self.length == 0:
            self.head = self.tail = Node(item)
            self.length += 1
        else:
            node = Node(item)
            node.next = self.head
            self.head = node
            self.length += 1

    def add_last(self, item):
        if self.length == 0:
            self.add_first(item)
        else:
            node = Node(item)
            node.next = None
            self.tail.next = node
            self.tail = node
            self.length += 1

    def remove_first(self):
        if self.head is None:
            raise Exception('List is empty.')
        self.head = self.head.next
        self.length -= 1

    def search(self, item):
        node = self.head
        while node:
            if node.data == item:
                return True
            node = node.next
        return False

    def print_list(self):
        node = self.head
        while node:
            print(node, end=" ")
            node = node.next
        print()
