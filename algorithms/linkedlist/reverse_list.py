"""Reverse a singly linked list.

Time: O(n)
Space: O(1)
"""


# iterative
def reverse_list(head):
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


# recursive
def reverse_list(head, prev=None):
    if not head:
        return prev
    curr, head.next = head.next, prev
    return reverse_list(curr, head)


"""Reverse a singly linked list from indices m to n.

Idea:
1. Find list[m:n], reverse it
2. Link m with n+1
3. Link n with m-1
"""


def reverse_list(head, m, n):
    if m == n:
        return head

    # use pointer p to 'create' the list we return
    dummy = p = Node(0)
    dummy.next = head

    for _ in range(m - 1):
        p = p.next

    # reverse list[m:n]
    prev, curr = None, p.next
    for _ in range(n - m + 1):
        curr.next, prev, curr = prev, curr, curr.next

    p.next.next = curr  # link m with n+1
    p.next = prev  # link m-1 with n

    return dummy.next
