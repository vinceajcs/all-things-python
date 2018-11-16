"""Given an n-ary tree, return the level order traversal of its nodes' values."""


def level_order(root):
    level, result = [root], []

    while any(level):
        current = []
        for node in level:
            current.append(node.val)

        result.append(current)

        level = [child for node in level for child in node.children if child]

    return result
