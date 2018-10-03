"""Compute the nth Fibnoacci number using linear recursion."""


def fibonacci(n):
    """Returns pair of Fibonacci numbers, F(n) and F(n-1) in linear time."""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n - 1)
        return (a + b, a)


"""Using dynamic programming."""


def fibonacci(n):
    result = [0] * n
    result[0], result[1] = 0, 1

    for i in range(2, n):
        result[i] = result[i - 1] + result[i - 2]

    return result[n]
