"""Given two lists A and B, where B is an anagram of A, find an index mapping result, from A to B.
A mapping result[i] = j means the ith element in A appears in B at index j.
These lists A and B may contain duplicates. If there are multiple answers, output any of them.

Example:

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

result = [1, 4, 3, 2, 0]

We can iterate through B and use a dict to store the index of each element.

Time: O(n)
Space: O(n)
"""


def anagram_mappings(A, B):
    if not A or not B:
        return []

    result = []

    lookup = collections.defaultdict(int)

    for i, n in enumerate(B):
        lookup[n] = i

    for n in A:
        result.append(lookup[n])

    return result
