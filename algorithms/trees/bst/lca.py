"""Given a BST, find the lowest common ancestor of two given nodes in the BST.

Time: O(n)
Space: O(1) 
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


# recursive
def lowest_common_ancestor(root, p, q):
    if not root or not p or not q:
        return None

    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root
