# recursive
def postorder(root, result=None):
    if root is None:
        return []
    if result is None:
        result = []

    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.val)

    return result


# iterative (reverse preorder)
def postorder(root):
    if not root:
        return []

    result, stack = [], []
    stack.append(root)

    while stack:
        root = stack.pop()
        result.append(root.val)

        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

    return result[::-1]  # return reversed result list
