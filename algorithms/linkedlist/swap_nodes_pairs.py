"""Given a linked list, swap every two adjacent nodes and return its head.

Idea: Transform from pre -> a -> b -> b.next to pre -> b -> a -> b.next.

Time: O(n)
Space: O(1)
"""


def swap_pairs(head):
    pre = dummy = Node(0)
    dummy.next = head

    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a

    return dummy.next
