"""Given a string, find the first unique character in it and return its index.
If a unique character doesn't exist, return -1.

Time: O(n)
Space: O(n)
"""


def first_unique_character(s):
    if not s:
        return -1

    lookup = collections.defaultdict(int)  # character -> index
    candidates = set()

    for i, c in enumerate(s):
        if lookup[c]:  # c is not unique
            candidates.discard(lookup[c])
        else:
            lookup[c] = i + 1
            candidates.add(i + 1)

    return min(candidates) - 1 if candidates else -1
