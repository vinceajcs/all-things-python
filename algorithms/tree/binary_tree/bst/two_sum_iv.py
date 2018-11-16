"""Classic two sum problem but this time input is the root node of a BST."""


def two_sum(root):
    if not root:
        return False

    return helper(root, set(), k)


def helper(node, node_set, k):
    if not node:
        return False

    complement = k - node.val
    if complement in node_set:
        return True

    node_set.add(node.val)

    return helper(node.left, node_set, k) or helper(node.right, node_set, k)
