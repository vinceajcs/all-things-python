"""Given an integer, determine if it is a power of two."""


def is_power_of_two(n):
    if n > 1:
        while n % 2 == 0:
            n /= 2
    return n == 1


"""Using bit manipulation."""


def is_power_of_two(n):
    return n & (n - 1) == 0
