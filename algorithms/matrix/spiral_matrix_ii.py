"""Given n, generate a n by n square matrix filled with elements 1 to n**2, in spiral order.

Idea:
Initialize n by n matrix with all zeroes, then walk the spiral path and write the numbers 1 to n**2.
If the cell ahead is nonzero, then make a 'right turn'.

Time: O(n**2)
Space: O(1)
"""


def generate_matrix(n):
    A = [[0 for _ in range(n)] for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1

    for k in range(n**2):
        A[i][j] = k + 1

        # check if cell ahead is nonzero
        if A[(i + di) % n][(j + dj) % n]:
            di, dj = dj, -di

        i += di
        j += dj

    return A


"""Another way based on first spiral matrix problem."""


def generate_matrix(n):
    A = [[0 for _ in range(n)] for _ in range(n)]

    left, right, top, bottom, num = 0, n - 1, 0, n - 1, 1

    while left <= right and top <= bottom:
        for j in range(left, right + 1):
            A[top][j] = num
            num += 1

        for i in range(top + 1, bottom):
            A[i][right] = num
            num += 1

        for j in reversed(range(left, right + 1)):
            if top < bottom:
                A[bottom][j] = num
                num += 1

        for i in reversed(range(top + 1, bottom)):
            if left < right:
                A[i][left] = num
                num += 1

        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

    return A


"""Another way by building matrix inside out.
1. Start with empty matrix, then add numbers in reverse order until we add the number 1.
2. For each iteration, rotate matrix clockwise (90 degrees, like in rotate image) and add the top row.
"""


def generate_matrix(n):
    A, start = [], n * n + 1

    while start > 1:
        start, end = start - len(A), start
        A = [list(range(start, end))] + [*zip(*A[::-1])]

    return A
