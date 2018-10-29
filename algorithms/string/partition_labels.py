"""Given a string, partition the string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.

Time: O(n)
Space: O(26) -> O(1)
"""


def partition_labels(s):
    lookup = {c: i for i, c in enumerate(s)}  # store each char's last index

    start = end = 0

    result = []

    for i, c in enumerate(s):
        end = max(end, lookup[c])

        if i == end:  # found a partition
            result.append(i - start + 1)
            start = i + 1

    return result
