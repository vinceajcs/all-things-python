"""Find the longest common prefix string among a list of strings.

Time: O(m*n), where m = len(shortest)
Space: O(1)
"""


def longest_common_prefix(strings):
    if not strings:
        return ''

    shortest = min(strings, key=len)  # get shortest string

    for i, c in enumerate(shortest):
        for s in strings:
            if s[i] != c:
                return shortest[:i]

    return shortest
