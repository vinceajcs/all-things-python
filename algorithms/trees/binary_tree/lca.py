"""Given a binary tree, find the lowest common ancestor of two given nodes in the BST.

Time: O(n)
Space: O(h)
"""


# recursive
def lowest_common_ancestor(root, p, q):
    if root in (None, p, q):
        return root

    left, right = [lowest_common_ancestor(child, p, q) for child in (root.left, root.right)]

    """
    1. If the current subtree contains both p and q,
        return their LCA.
    2. If only one of them is in that subtree,
        return that one.
    3. If neither of them is in that subtree,
        return the node of that subtree.
    """
    return root if left and right else left or right
