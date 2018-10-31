"""Given a string, reverse only the vowels of the string.

Time: O(n)
Space: O(1)
"""


def reverse_vowels(s):
    if not s:
        return ''

    vowels = set('AEIOUaeiou')
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        while s[i] not in vowels and i < j:
            i += 1
        while s[j] not in vowels and i < j:
            j -= 1

        s[i], s[j] = s[j], s[i]

        i += 1
        j -= 1

    return ''.join(s)
