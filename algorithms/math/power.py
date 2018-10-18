"""Implement power(x, n), which calculates x raised to the power n (x**n)."""


def power(x, n):
    if n == 0:
        return 1

    if n < 0:
        n = -n
        x = 1 / x

    return power(x * x, n // 2) if (n % 2 == 0) else x * power(x * x, n // 2)


"""Using repeated squaring (both time and space complexity: O(logn)).
power(x, n) = 1 if n = 0,
              x * (power(x, n//2))**2 if n > 0 is odd,
              (power(x, n//2))**2     if n > is even.
"""


def power(x, n):
    """Note: this assumes both x and n are nonnegative integers."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial

        if n % 2 == 1:
            result *= x

        return result


"""Using simple recurison."""


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
