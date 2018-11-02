"""Given an integer, determine if it is a power of three."""


# iterative
def is_power_of_three(n):
    if n > 1:
        while n % 3 == 0:
            n /= 3

    return n == 1


# recurisve
def is_power_of_three(n):
    return n > 0 and (n == 1 or (n % 3 == 0 and is_power_of_three(n / 3)))


"""Using the fact that 1162261467 is the max power of 3."""


def is_power_of_three(n):
    return n > 0 and (1162261467 % n == 0)
