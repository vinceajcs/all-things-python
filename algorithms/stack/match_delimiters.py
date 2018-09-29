def is_matched(expr):
    """Return True if all delimiters are properly matched; False otherwise. Running time is linear."""
    left = '({['
    right = ')}]'
    stack = []

    for e in expr:
        if e in left:
            stack.push(e)
        elif e in right:
            if not stack:
                return False
            if right.index(e) != left.index(stack.pop()):
                return False

    return False if stack else True
