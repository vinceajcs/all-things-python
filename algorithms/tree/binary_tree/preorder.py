# recursive
def preorder(root, result=None):
    if root is None:
        return []
    if result is None:
        result = []

    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)

    return result


# iterative
def preorder(root):
    if not root:
        return []

    result, stack = [], []
    stack.append(root)

    while stack:
        root = stack.pop()
        result.append(root.val)

        # preorder is root, left, right, but stack is LIFO so add right subtree first
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

    return result
