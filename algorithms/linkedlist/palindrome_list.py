"""Given a singly linked list, determine if it is a palindrome.

Time: O(n)
Space: O(1)
"""


def is_palindrome(head):
    # find midpoint of list
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # slow now points to midpoint of list

    # reverse second half of list
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # compare first and second half of list
    l1, l2 = head, prev
    while l2:
        if l2.val != l1.val:
            return False
        l1, l2 = l1.next, l2.next

    return True


"""We can also use extra space to solve this."""


def is_palindrome(head):
    if head is None:
        return True

    nodes = []

    while head:
        nodes.append(head.val)
        head = head.next

    # check if list is equal to its reverse (definition of palindrome)
    if nodes == nodes[::-1]:
        return True

    return False
