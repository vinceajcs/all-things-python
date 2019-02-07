"""Given a string, your task is to count how many palindromic substrings are in the string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of the same characters.

Naive idea:
1. Get all substrings
2. Check if substring is a palindrome
3. Count the number of palindromic substrings

Better idea: expand from center for each center at index i in string s.

Note: this can also be solved using Manacher's algorithm (linear time complexity). This is not implemented here.

Time: O(n**2)
Space: O(1)
"""


def count_substrings(s):
    if not s:
        return 0

    def is_palindrome(x): return x == x[::-1]  # same as lambda x : x == x[::-1]

    count = 0

    substrings = get_substrings(s)
    for substring in substrings:
        if is_palindrome(substring):
            count += 1

    return count


def get_substrings(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            yield s[i:j]  # returns a generator, a type of iterator


"""Another way to find palindromes by expanding from center.
Note: There are 2n-1 centers; a center of a palindrome can be in-between two chars (e.x., in 'abba', the center is between the b's).
For each middle pivot position, you need to check it twice: once that includes the character and once without the character."""


def count_substrings(s):
    count, n = 0, len(s)

    for i in range(2 * n - 1):
        left, right = i // 2, (i + 1) // 2

        # find palindromes by expanding from center for each center at index i
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count
