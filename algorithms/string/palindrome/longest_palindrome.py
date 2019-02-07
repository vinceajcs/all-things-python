"""Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

For each letter, say it occurs v times. We know we have v // 2 * 2 letters that can be partnered for sure.
For example, if we have 'aaaaa', then we could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.
At the end, if there was any v % 2 == 1, then that letter could have been a unique center. Otherwise, every letter was partnered.
To perform this check, we will check for v % 2 == 1 and ans % 2 == 0, the latter meaning we haven't yet added a unique center to the answer.

Note: Each palindrome can contain at most one char with an odd frequency!

Time: O(n)
Space: O(n)
"""


def longest_palindrome(s):
    if not s:
        return 0

    counter = collections.Counter(s)

    longest = 0
    odd_chars = 0

    for freq in counter.values():
        longest += freq // 2 * 2

        if freq % 2 == 1 and not odd_chars:
            longest += 1
            odd_chars += 1

    return longest
