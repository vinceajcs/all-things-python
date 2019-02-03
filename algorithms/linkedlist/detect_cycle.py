"""Given a linked list, determine if it has a cycle in it.

Idea: Use two pointers, where one pointer increments twice as much as the other.
If the two pointers meet, then there is a cycle!

Time: O(n)
Space: O(1)
"""


def detect_cycle(head):
    if not head:
        return False

    fast, slow = head, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast is slow:
            return True

    return False


"""Determine where the cycle starts, if there is one."""


def detect_cycle(head):
    fast, slow = head, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast is slow:
            fast = head
            while fast is not slow:
                fast, slow = fast.next, slow.next
            return fast

    return None
