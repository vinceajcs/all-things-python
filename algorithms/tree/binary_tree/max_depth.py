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

    max_depth, level, depths = 0, [root], [1]

    while level:
        next_level = []
        depth = depths.pop()
        max_depth = max_depth if max_depth > depth else depth

        for node in level:
            left, right = node.left, node.right

            if left:
                next_level.append(left)
                depths.append(depth + 1)
            if right:
                next_level.append(right)
                depths.append(depth + 1)

        level = next_level

    return max_depth
