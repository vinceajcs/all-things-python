"""Given a sorted linked list, delete all duplicates such that each element appear only once.

Time: O(n)
Space: O(1)
"""


def delete_duplicates(head):
    curr = head
    while curr:
        while curr.next and curr.next.val == curr.val:
            # delete duplicate
            curr.next = curr.next.next
        curr = curr.next
    return head


"""Same problem as above, but this time only return nodes with distinct values from the original list.
Here, we use the pointer p to 'create' the list of distinct nodes.
"""


def delete_duplicates(head):
    dummy = p = Node(0)
    dummy.next = head
    curr = head

    while curr:
        if curr.next and curr.next.val == curr.val:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            p.next = curr.next
        else:
            p = p.next

        curr = curr.next

    return dummy.next
