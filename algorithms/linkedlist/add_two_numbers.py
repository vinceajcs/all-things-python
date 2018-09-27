"""You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Time: O(n)
Space: O(1)
"""


def add_two_numbers(l1, l2):
    dummy = p = Node(0)
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        p.next = Node(carry % 10)
        p = p.next
        carry //= 10

    return dummy.next
