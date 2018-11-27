"""Find the node at which the intersection of two singly linked lists begins. Assume there are no cycles.

Idea: Use two pointers, p1 and p2 to traverse the lists l1 and l2, respectively.
1. When p1 reaches the end of l1, redirect it to point to the head of l2.
Similarly, when p2 reaches the end of l2, redirect it to point to the head of l1.
2. If at any point p1 = p2 (both point to same node), then p1/p2 is the intersection node.

Note: if l1 and l2 intersect, then the last node of each list must be the same.


Time: O(m+n)
Space: O(1)
"""


def get_intersection_node(l1, l2):
    if l1 is None or l2 is None:
        return None

    p1, p2 = l1, l2

    """By switching heads, the possible difference in length between l1 and l2 is accounted for.
    On the second traversal, the pointers either hit or miss.
    If they meet, p1 or p2 points to the node we are looking for.
    Otherwise, p1 == p2 == None.
    """

    while p1 is not p2:
        p1 = l2 if p1 is None else p1.next
        p2 = l1 if p2 is None else p2.next

    return p1
