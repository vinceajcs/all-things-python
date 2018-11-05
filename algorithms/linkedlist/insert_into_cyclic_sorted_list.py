"""Given a node from a cyclic linked list which is sorted in ascending order, insert a value into the list such that it remains a cyclic sorted list.
The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.
If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.

There are two cases to consider:
1. The value to be inserted can be placed between two nodes (prev and curr).
2. The value to be inserted is either the max or the min of the linked list (value > prev or value < curr).

Time: O(n)
Space: O(1)
"""


def insert_node(head, x):
    new_node = Node(x, None)

    if not head:
        new_node.next = new_node
        return new_node

    prev, curr = head, head.next

    while curr != head:
        if prev.val <= x <= curr.val:  # first case
            break

        if prev.val > curr.val and (x < curr.val or x > prev.val):  # second case
            break

        curr, prev = curr.next, prev.next

    # insert node into list
    prev.next = new_node
    new_node.next = curr

    return head
