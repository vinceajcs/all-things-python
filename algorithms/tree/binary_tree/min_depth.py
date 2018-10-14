"""Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Idea:
For each subtree, add the minimum of the children's depths if there is both a left and right child.
Otherwise add the maximum.

Time: O(n)
Space: O(h)
"""


# recursive
def min_depth(root):
    if root is None:
        return 0

    if root.left and root.right:
        return min(min_depth(root.left), min_depth(root.right)) + 1
    else:
        return max(min_depth(root.left), min_depth(root.right)) + 1


# iterative
def min_depth(root):
    if not root:
        return 0

    depth, level = 0, [root]

    while level:
        depth += 1
        next_level = []

        for node in level:
            left, right = node.left, node.right

            if not left and not right:
                return depth

            if left:
                next_level.append(left)
            if right:
                next_level.append(right)

        level = next_level

    return depth
