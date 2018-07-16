class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()


def print_backward(list):
    if list is None:
        return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print_list(node1)
print_backward(node1)
