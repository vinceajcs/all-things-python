"""Given a string s, find the longest palindromic substring in s.

Idea: at each index i of s, expand from center (which is i) to find the longest palindrome that can be made with i.
Note: There are 2n-1 centers; a center of a palindrome can be in-between two chars (e.x., in 'abba', the center is between the b's).

Time: O(n**2)
Space: O(1)
"""


def longest_palindromic_substring(s):
    substring = ""

    for i in range(len(s)):
        # get longest palindrome for odd case, like 'aba'
        temp = helper(s, i, i)
        if len(temp) > len(substring):
            substring = temp

        # get longest palindrome for even case, like 'abba'
        temp = helper(s, i, i + 1)
        if len(temp) > len(substring):
            substring = temp

    return substring


def helper(s, l, r):
    # find longest palindrome by expanding from center of string s
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1

    return s[l + 1:r]
