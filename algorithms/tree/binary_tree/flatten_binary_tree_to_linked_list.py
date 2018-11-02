"""Given a binary tree, flatten it to a linked list in-place.

Idea:
1. Flatten left subtree
2. Find left subtree's tail (end)
3. Set root's left to None, root's right to root's left subtree, and tail's right to root's right subtree
4. Flatten original right subtree

Time: O(n)
Space: O(n)
"""


def flatten(root):
    if not root:
        return

    right = root.right

    if root.left:
        flatten(root.left)  # flatten left subtree

        tail = root.left  # get left subtree's tail
        while tail.right:
            tail = tail.right

        root.left, root.right, tail.right = None, root.left, right

    flatten(root.right)


"""Another way."""


pre = None


def flatten(root):
    if not root:
        return

    flatten(root.right)
    flatten(root.left)

    root.right = pre
    root.left = None
    pre = root
