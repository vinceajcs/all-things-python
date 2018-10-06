def level_order(root):
    if root is None:
        return []

    level, result = [root], []

    while level:
        current, next_level = [], []
        for node in level:
            current.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        result.append(current)

    return result
