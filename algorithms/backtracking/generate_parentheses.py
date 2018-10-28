"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Some thoughts:
In a balanced string of parentheses, the count of ')' must always be less than or equal to the count of '(',
for every prefix of the string.

We can add '(' before ')' for every recursive state string (prefix) until the count of '(' = n.
Then we can start adding closing brackets with the conidition that the number of closing brackets does not exceed that of the opening ones.

Time: O(4**n)
Space: O(n)
"""


def generate_parenthesis(n):
    if not n:
        return []
    left, right, result = n, n, []
    dfs(left, right, result, '')
    return result


def dfs(self, left, right, result, string):
    if right < left:
        return
    if not left and not right:  # found a valid combination
        result.append(string)
        return
    if left:
        dfs(left - 1, right, result, string + '(')
    if right:
        dfs(left, right - 1, result, string + ')')
