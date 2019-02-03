"""Given a singly linked list, group all odd nodes together followed by the even nodes.

Note: The first node is considered odd.

Time: O(n)
Space: O(1)
"""


def odd_even_list(head):
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)

    i = 1  # index to keep track of list nodes

    while head:
        if i % 2:
            odd.next, odd = head, head
        else:
            even.next, even = head, head
        head = head.next
        i += 1

    # connect list of odd nodes with list of even nodes
    odd.next, even.next = dummy2.next, None

    return dummy1.next
