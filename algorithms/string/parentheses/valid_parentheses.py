"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.
Note that an empty string is also considered valid.

Idea: Use a stack + dict.

Time: O(n)
Space: O(n)
"""


def is_valid(s):
    # string can't be valid if it has an odd number of chars
    if len(s) % 2 != 0:
        return False

    stack = []
    lookup = {']': '[', '}': '{', ')': '('}

    for char in s:
        if char in lookup.values():
            stack.append(char)
        elif char in lookup.keys():
            if not stack or lookup[char] != stack.pop()
                return False
        else:
            return False

    return len(stack) == 0
