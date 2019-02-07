"""Given two strings s and t, write a function to determine if t is an anagram of s.

Idea: Two strings are considered anagrams of each other if they have the same frequency of each character.
Thus, we can use two dicts to count the number of chars in each string and check if the dicts are equal.

Time: O(n)
Space: O(1)
"""


from collections import Counter  # Counter is a type of dict


def is_anagram(s, t):
    if len(t) != len(s):
        return False

    counter_s, counter_t = Counter(s), Counter(t)

    # could alternatively return counter_s == counter_t here without any of the code below

    for key, value in counter_s.items():
        if counter_t[key] != value:
            return False

    return True


"""Using standard dict instead of Counter."""


def is_anagram(s, t):
    lookup_s, lookup_t = {}, {}

    for c in s:
        lookup_s[c] = lookup_s.get(c, 0) + 1
    for c in t:
        lookup_t[c] = lookup_t.get(c, 0) + 1

    return lookup_s == lookup_t


"""Using Python's built-in sorted function."""


def is_anagram(s, t):
    return sorted(s) == sorted(t)
