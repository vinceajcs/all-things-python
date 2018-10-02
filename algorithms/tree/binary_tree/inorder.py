# recursive
def inorder(root, result=None):
    if root is None:
        return []
    if result is None:
        result = []

    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)

    return result


# iterative
def inorder(root):
    if not root:
        return []

    result, stack = [], []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right

    return result
