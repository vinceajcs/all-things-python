"""Given a singly linked list L: L0→L1→...→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→...

Time: O(n)
Space: O(1)
"""


def reorder(head):
    if not head:
        return

    # find midpoint of list
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # reverse second half of list
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # merge
    """Here l1 points to the head of the first half of list, while l2 points to the head of the second half.
    Idea is to make l1's next element l2, then advance l1. Similarly, we make l2's next element l1 and then advance l2.
    """
    l1, l2 = head, prev
    while l2.next:
        l1.next, l1 = l2, l1.next
        l2.next, l2 = l1, l2.next

    return
