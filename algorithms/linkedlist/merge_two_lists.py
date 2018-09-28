"""Merge two sorted linked lists and return it as a new list.

Time: O(n)
Space: O(1)
"""


# iterative
def merge_two_lists(l1, l2):
    # we use p to 'create' the list we return
    dummy = p = Node(0)

    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next

        p = p.next

    p.next = l1 or l2  # whichever list still has a node left

    return dummy.next


# recursive
def merge_two_lists(l1, l2):
    if not l1 or not l2:
        return l1 or l2

    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
