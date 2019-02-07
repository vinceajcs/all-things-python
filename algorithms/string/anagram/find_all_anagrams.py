"""Given a string s and a non-empty string t, find all the start indices of t's anagrams in s.

We can use the sliding window technique with a dict.

Time: O(n)
Space: O(1)
"""


def find_anagrams(s, t):
    count_t, count_s = collections.Counter(t), collections.Counter(s[:len(t) - 1])

    result = []

    for i in range(len(t) - 1, len(s)):
        count_s[s[i]] += 1  # include new char in window

        if count_t == count_s:  # found an anagram
            result.append(i - len(t) + 1)  # append starting index

        count_s[s[i - len(t) + 1]] -= 1  # decrease freq count of oldest char in window

        if count_s[s[i - len(t) + 1]] == 0:
            del count_s[s[i - len(t) + 1]]

    return result
