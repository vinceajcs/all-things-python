"""Given a positive integer n, find the least number of perfect square numbers (1, 4, 9, 16,...) which sum to n.

Let squares(i) = min number of perfect squares that sum to i.

squares(i) = 0 if i = 0
             min(squares(i), squares(i-j*j)+1) o.w.

Each number i has to be the sum of a perfect square (j*j) and some number (i-j*j).

Time: O(n*sqrt(n))
Space: O(n)
"""


def perfect_squares(n):
    if not n:
        return 0

    squares = [float('inf') for _ in range(n + 1)]
    squares[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j < n + 1:
            squares[i] = min(squares[i], squares[i - j * j] + 1)
            j += 1

    return squares[-1]
