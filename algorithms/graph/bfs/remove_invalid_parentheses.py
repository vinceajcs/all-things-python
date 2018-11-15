"""Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than parentheses.

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Time: O(2**n)
Space: O(n)
"""


def remove_invalid_parentheses(s):
    level = {s}

    while True:
        valid = [s for s in level if is_valid(e)]
        if valid:
            return valid

        level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}
        """Same as:
        next_level = set()
        for s in level:
            for i in range(len(s)):
                next_level.add(s[:i] + s[i+1:])
        # next_level = {'(())()', '()()()', ')())()', '()()))', '()))()', '()())('}
        level = next_level
        """


def is_valid(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0
