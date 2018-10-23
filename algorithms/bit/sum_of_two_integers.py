"""Calculate the sum of two integers a and b without using the operators + and -."""


def get_sum(a, b):
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    mask = 0xFFFFFFFF

    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    return a if a <= MAX else ~(a ^ mask)
