"""A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.

Time: O(n)
Space: O(n)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def copy_list(head):
    if not head:
        return None

    lookup = collections.defaultdict(lambda: Node(0))
    lookup[None] = None

    # copy all nodes
    node = head
    while node:
        lookup[node] = Node(node.label)
        node = node.next

    # assign next and random pointers
    node = head
    while node:
        lookup[node].next = lookup[node.next]
        lookup[node].random = lookup[node.random]
        node = node.next

    return lookup[head]
