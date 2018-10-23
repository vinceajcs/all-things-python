"""Given a non negative integer number, calculate the number of 1's in the binary representation for every number i in the range 0 ≤ i ≤ n and return them as a list.

Time: O(n)
Space: O(1)
"""


def count_bits(n):
    result = [0]
    while len(result) <= n:
        result += [i + 1 for i in result]
    return result[:n + 1]


def count_bits(n):
    result = [0]
    for i in range(1, n + 1):
        # add previous result with one less 1
        result.append(result[i & (i - 1)] + 1)
    return result


def count_bits(n):
    result = [0]
    for i in range(1, n + 1):
        # number of 1s in i = (i&1) + number of 1s in (i/2)
        result.append(i & 1 + result[i >> 1])
    return result
