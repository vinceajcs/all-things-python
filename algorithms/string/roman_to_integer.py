"""Given a roman numeral, convert it to an integer.

Time: O(n)
Space: O(1)
"""


def roman_to_integer(s):
    lookup = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}

    prev = 0
    result = 0

    for i in range(len(s)-1, -1, -1):
        current = lookup[s[i]]

        if current < prev:
            result -= current
        else:
            result += current

        prev = current

    return result
