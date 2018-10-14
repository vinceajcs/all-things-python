# recursive
def is_same(p, q):
    if p and q:
        return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)
    else:
        return p is q  # same as True if p == None and q == None else False


# iterative
def is_same(p, q):
    stack = [(p, q)]

    while stack:
        n1, n2 = stack.pop()

        if n1 and n2 and n1.val == n2.val:
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        elif not n1 and n2:
            continue
        else:
            return False

    return True
