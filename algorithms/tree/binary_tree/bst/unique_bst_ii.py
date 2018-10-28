"""Same as unique bst, but here we generate unique BSTs instead of the number of them."""


def unique_bst(n):
    if not n:
        return []
    return generate_subtrees(1, n)


def generate_subtrees(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_subtrees = generate_subtrees(start, i - 1)
        right_subtrees = generate_subtrees(i + 1, end)

        for left in left_subtrees:
            for right in right_subtrees:
                root = Node(i)
                root.left = left
                root.right = right
                result.append(root)

    return result
