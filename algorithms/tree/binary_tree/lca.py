"""Given a binary tree, find the lowest common ancestor of two given nodes in the binary tree.

Time: O(n)
Space: O(h)
"""


# recursive
def lowest_common_ancestor(root, p, q):
    if root in (None, p, q):
        return root

    # search subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:  # both are found in the subtree, root is LCA
        return root

    return left or right  # either root of left or right subtree is LCA


# iterative
def lowest_common_ancestor(root, p, q):
    if not root:
        return root

    stack = [root]
    parents = {root: None}

    # keep track of parents
    while p not in parents or q not in parents:
        node = stack.pop()

        if node.left:
            parents[node.left] = node
            stack.append(node.left)
        if node.right:
            parents[node.right] = node
            stack.append(node.right)

    ancestors = set()

    # get all of p's ancestors
    while p:
        ancestors.add(p)
        p = parents[p]

    # go through q's ancestors to see if any of them is an ancestor of p
    while q not in ancestors:
        q = parents[q]

    return q
