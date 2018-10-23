"""Reverse bits of a given 32 bits unsigned integer.

Time: O(32)
Space: O(1)
"""


def reverse_bits(n):
    if not n:
        return 0
    result = 0

    for i in range(32):
        result <<= 1
        if n & 1 == 1:
            result += 1
        n >>= 1

    return result
