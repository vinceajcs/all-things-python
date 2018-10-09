"""Given a binary tree, determine if it is a BST.

We can solve this by performing an inorder traversal of the binary tree.
If a previous node has a value greater or equal to a current node, then the binary tree is not a BST.

Time: O(n)
Space: O(1)
"""


def is_valid_bst(root):
    if not root:
        return True

    stack = []
    pre = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if pre and root.val <= pre.val:
            return False
        pre = root
        root = root.right

    return True
