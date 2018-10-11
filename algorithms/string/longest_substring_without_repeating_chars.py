"""Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Naive: Check if each possible substring has repeating characters. This is O(n**3).

Better idea: Use the sliding window technique.
1. If a substring s from index i to j-1 has already been checked to have no duplicates, we just need to check if s[j] is a duplicate.
2. We can use a set to keep track of which characters we have seen in a current window, and check the set to see if s[j] is a duplicate.
3. If s[j] is not a duplicate, we update the length and move the right pointer j forward to the next character.
4. If s[j] is a duplicate, we remove s[i] from the set and move the left pointer i forward.

Time: O(n)
Space: O(min(m, n)), where m is the size of set and n is the length of the input string.
"""


def length_of_longest_substring(s):
    if not s:
        return 0

    # set used to keep track of which chars are in a current window
    used_chars = set()
    # i and j are the left and right pointers, respectively
    max_length, i, j = 0, 0, 0

    while i < len(s) and j < len(s):
        # advance right pointer
        if s[j] not in used_chars:
            used_chars.add(s[j])
            j += 1
            max_length = max(max_length, j - i)
        else:
            # advance left pointer
            used_chars.remove(s[i])
            i += 1

    return max_length
