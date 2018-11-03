"""Given a BST, find the second largest element.

Time: O(h)
Space: O(1)
"""


def find_largest(root):
    current = root
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root):
    if not root or not root.left or root.right:
        return

    current = root
    while current:
        # current is the rightmost node and has a left subtree
        # then, 2nd largest node is the largest in that left subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # current is parent of the largest node, and largest has no children
        # then, current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right
