"""Given a string s and a string t, check if s is subsequence of t.

Time: O(n)
Space: O(1)
"""


def is_subsequence(s, t):
    if len(s) == 0:
        return True
    if len(t) == 0:
        return False

    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return True if i == len(s) else False


"""Using an iterator."""


def is_subsequence(s, t):
    iter = iter(t)
    return all(c in iter for c in s)
