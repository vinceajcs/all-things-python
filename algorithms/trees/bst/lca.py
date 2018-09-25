"""Given a BST, find the lowest common ancestor of two given nodes in the BST.

Time: O(n)
Space: O(1) iterative
"""


# iterative
def lowest_common_ancestor(root, p, q):
    if root in (None, p, q):
        return root

    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
