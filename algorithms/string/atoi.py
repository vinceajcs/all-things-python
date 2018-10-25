"""Implement atoi, which converts a string into an integer.

Time: O(n)
Space: O(1)
"""


def atoi(s):
    s = s.strip()  # strip whitespace chars at beginning + end of string
    s = re.findall('^[+\-]?\d+', s)  # findall returns a list of strings

    try:
        result = int(''.join(s))
        MAX = 2147483647
        MIN = -2147483648

        if result > MAX:
            return MAX
        if result < MIN:
            return MIN
        return result

    except:
        return 0
