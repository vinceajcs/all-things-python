"""Given a string, determine if a permutation of that string could form a palindrome.

Observations:
If a string is a palindrome:
    If string is even length -> every char in the string must occur an even number of times
    If string is odd length -> every char EXCEPT one must occur an even number of times

Thus, the number of chars in a string with an odd number of occurences cannot exceed 1 (1 for odd length, 0 for even), for the string to be a palindrome.

Time: O(n)
Space: O(n)
"""


def is_palindrome_permutation(s):
    lookup = collections.Counter(s)

    odd_chars = 0

    for char, freq in lookup.items():
        if freq % 2 != 0:
            odd_chars += 1

    return odd_chars <= 1


"""Without using a dictionary."""


def is_palindrome_permutation(s):
    odd_chars = 0

    for i in range(128):
        count = 0  # record number of occurences in s for char i
        for j in range(len(s)):
            if ord(s[j]) == i:
                count += 1

        odd_chars += count % 2

    return odd_chars <= 1
