def zigzag_level(root):
    if not root:
        return []

    level, result = [root], []
    zigzag = 1

    while level:
        next_level, current = [], []
        for node in level:
            current.append(node.val)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            level = next_level
            result.append(current[::zigzag])
            zigzag *= -1

    return result
