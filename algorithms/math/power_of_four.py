"""Given an integer, determine if it is a power of four."""


def is_power_of_four(n):
    if n > 1:
        while n % 4 == 0:
            n /= 4

    return n == 1
