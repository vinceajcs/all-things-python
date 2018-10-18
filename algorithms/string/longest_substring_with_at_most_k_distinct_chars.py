"""Given a string, find the length of the longest substring that contains at most k distinct characters.

Idea: Sliding window with a dict. Use left and right pointer track window.
1. Advance right pointer, one char at a time, until it reaches the end of the string.
2. At each iteration of the right pointer, if there are more than k distinct chars, move left pointer to remove chars in current window.

Time: O(n)
Space: O(n)
"""


def longest_substring_k_distinct(s, k):
    if not s or not k:
        return 0

    i, max_length = 0, 0

    lookup = collections.defaultdict(int)

    for j in range(len(s)):
        lookup[s[j]] += 1

        if len(lookup) > k:  # start removing characters from left
            lookup[s[i]] -= 1

            if lookup[s[i]] == 0:
                del lookup[s[i]]

            # move left pointer
            i += 1

        max_length = max(max_length, j - i + 1)

    return max_length
