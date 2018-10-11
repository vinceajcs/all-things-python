"""Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Idea: Categorize anagrams by sorted string.
Use a dict of key = tuple of sorted string, value = list of strings, that when sorted, equal the key.

Time: O(nklogk)
Space: O(nk)

n = length of string list
k = max length of string in string list
"""


def group_anagrams(strings):
    result = collections.defaultdict(list)
    for s in strings:
        # have to use tuple because lists are not hashable (tuples are immutable, whereas lists are mutable)
        result[tuple(sorted(s))].append(s)
    return list(result.values())


"""Another way, where the keys of the dict are the character counts of the strings. This cancels the need for sorting."""


def group_anagrams(strings):
    result = collections.defaultdict(list)
    for s in strings:
        count = [0] * 26  # assuming alphabet of input is only 26 chars (a-z)
        for c in s:
            # create key
            index = ord(c) - ord('a')
            count[index] += 1
        # add to dict
        result[tuple(count)].append(s)

    return list(result.values())
