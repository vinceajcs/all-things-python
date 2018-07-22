from stack import *


def is_matched(expr):
    """Return True if all delimiters are properly matched; False o.w.
    Running time is linear."""
    left = '({['
    right = ')}]'
    stack = Stack()

    for e in expr:
        if e in left:
            stack.push(e)
        elif e in right:
            if stack.is_empty():
                return False
            if right.index(e) != left.index(stack.pop()):
                return False

    return stack.is_empty()
