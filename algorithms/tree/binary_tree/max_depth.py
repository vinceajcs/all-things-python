"""Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the furthest leaf node.

Time: O(n)
Space: O(h)
"""


# recursive
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# iterative
def max_depth(root):
    if not root:
        return 0

    max_depth = 0
    level, depths = [root], [1]

    while level:
        next_level = []
        depth = depths.pop()
        max_depth = max_depth if max_depth > depth else depth

        for node in level:
            if node.left:
                next_level.append(node.left)
                depths.append(depth + 1)
            if node.right:
                next_level.append(node.right)
                depths.append(depth + 1)

        level = next_level

    return max_depth
