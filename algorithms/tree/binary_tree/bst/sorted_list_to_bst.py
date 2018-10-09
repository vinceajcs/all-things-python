"""Given an list with elements sorted in ascending order, convert it to a height balanced BST.

We can solve this by converting the linked list into an array, then build BST from array.

Time: O(n)
Space: O(logn)
"""


def sorted_list_to_bst(head):
    # build array
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return helper(array, 0, len(array) - 1)


def helper(array, start, end):
    if start > end:
        return None
    if start == end:
        return Node(array[start])

    mid = (start + end) // 2
    root = Node(array[mid])
    root.left = helper(array, start, mid - 1)
    root.right = helper(array, mid + 1, end)

    return root
