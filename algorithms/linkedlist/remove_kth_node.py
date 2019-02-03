"""Given a linked list, remove the kth node from the end of list and return its head.

Idea: Use two pointers, where one pointer is k nodes ahead of the other.
When that pointer reaches the end, the other pointer is k nodes behind.

Time: O(n)
Space: O(1)
"""


def remove_kth_node(head, k):
    slow, fast = head, head

    # advance fast pointer so that it is k nodes in front of slow
    for _ in range(k):
        fast = fast.next

    if not fast:  # deals with edge case(s)
        return head.next

    while fast.next:
        slow, fast = slow.next, fast.next

    # remove kth node
    slow.next = slow.next.next

    return head
