"""Given two strings s1 and s2, determine if s2 is a rotation of s1.

Time: O(n)
Space: O(1)
"""


def string_rotation(s1, s2):
    """s2 will always be a substring of s1 + s1 if s2 is a rotation of s1."""
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)
    return False


def is_substring(string, substring):
    return string.find(substring) != -1
