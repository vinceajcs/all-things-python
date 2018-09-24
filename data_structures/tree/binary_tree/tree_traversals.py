from collections import deque


def preorder(root, result=None):
    if root is None:
        return []
    if result is None:
        result = []

    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)

    return result


def inorder(root, result=None):
    if root is None:
        return []
    if result is None:
        result = []

    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)

    return result


def postorder(root, result=None):
    if root is None:
        return []
    if result is None:
        result = []

    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.val)

    return result


def breadth_first(root):
    queue = deque([root])
    while queue is not None:
        node = queue.popleft()

        print(node)  # process node here

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
