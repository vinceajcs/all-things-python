"""Given an input string s and a pattern s, implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

Time: O(m*n)
Space: O(m*n)
"""


"""Using recursion."""


def is_match(s, p):
    if not p: return not s

    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[i] == '*':  # wildcard (*) would need to be at the second position of the pattern
        # we could either ignore the pattern, or delete matching char from string
        return ((is_match(s, p[2:]) or (first_match and is_match(s[1:], p)))
    else:
        return first_match and is_match(s[1:], p[1:])


"""Using DP.

We can define dp(i, j) to be true if s[0...i) matches p[0...j) and false o.w.

dp(i, j) = dp(i-1, j-1)                                       if p(j-1) == '.'
           dp(i, j-2)                                         if p(j-1) == '*' and pattern repeats 0 times
           dp(i-1, j) and (s(i-1) == p(j-2) or p(j-2) == '.') if p(j-1) == '*' and pattern repeats 1+ times
           dp(i-1, j-1) and s(i-1) == p(j-1)                  o.w.
"""


def is_match(s, p):
    m, n=len(s), len(p)
    dp=[[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0]=True

    # match empty string with '.*'
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            if i >= 2:
                dp[0][i]=dp[0][i - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.':
                dp[i][j]=dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j]=dp[i][j - 2] or (dp[i - 1][j]
                                            and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
            else:  # p[j-1] is an lowercase letter from a-z
                dp[i][j]=dp[i - 1][j - 1] and s[i - 1] == p[j - 1]

    return dp[m][n]
