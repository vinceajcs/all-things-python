"""Given a binary tree, imagine yourself standing on the right side of it, and return the values of the nodes you can see ordered from top to bottom.

Time: O(n)
Space: O(1)
"""

"""DFS traversal from right to left. We can add a node to result whenever we reach a new depth."""


def right_side_view(root):

    def dfs(node, depth):
        if node:
            if depth == len(result):  # reached new depth
                result.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

    result = []
    dfs(root, 0, result)
    return result


"""Level order traversal, adding the last value of each level."""


def right_side_view(root):
    result = []

    if root:
        level = [root]
        while level:
            result.append(level[-1].val)
            level = [child for node in level for child in (node.left, node.right) if child]

    return result
