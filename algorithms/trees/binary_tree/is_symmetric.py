def is_symmetric(root):
    if root is None:
        return True

    return helper(root.left, root.right)


def helper(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None or left.val != right.val:
        return False

    return helper(left.left, right.right) and helper(left.right, right.left)


def is_symmetric(root):
    if root is None:
        return True

    stack = []
    stack.append(root.left)
    stack.append(root.right)

    while stack:
        p, q = stack.pop(), stack.pop()

        if p is None and q is None:
            continue
        if p is None or q is None or p.val != q.val:
            return False

        stack.append(p.left)
        stack.append(q.right)

        stack.append(p.right)
        stack.append(q.left)

    return True
