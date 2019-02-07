"""Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid.

We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Idea: Two passes through s (left -> right, then right -> left).
First pass, we check if there are enough ( to balance all the ), treating * as (.
Second pass, we check if there are enough ) to balance all the (, treating * as ).

Time: O(n)
Space: O(n)
"""


def is_valid(s):
    if not s:
        return True

    stack = []
    # iterate through s from left to right
    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        else:  # c is ')'
            if len(stack) > 0:
                stack.pop()
            else:
                return False  # we don't have enough '(' to balance ')'

    stack = []
    # iterate through s from right to left
    for c in s[::-1]:
        if c == ')' or c == '*':
            stack.append(c)
        else:  # c is '('
            if len(stack) > 0:
                stack.pop()
            else:
                return False  # we don't have enough ')' to balance '('

    return True


"""Using a Greedy algorithm."""


def is_valid(s):
    lo, hi = 0, 0
    for c in s:
        if c == "(":
            lo += 1
            hi += 1
        elif c == ")":
            lo -= 1
            hi -= 1
        elif c == "*":
            lo -= 1
            hi += 1
        if hi < 0:
            return False
        lo = max(lo, 0)
    return lo == 0
