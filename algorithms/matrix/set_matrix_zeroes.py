"""Given a m x n matrix, if an element is 0, set its entire row and column to 0.

Idea:
1. Find out which rows + columns contain 0, and record these in separate sets.
2. Change all elements in these rows + columns to 0.

Time: O(m*n)
Space: O(m+n) (for first solution), O(1) for second solution
"""


def set_zeroes(A):
    row_set, col_set = set(), set()

    # iterate matrix to record rows and cols
    m, n = len(A), len(A[0])

    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    # change all rows with 0 to 0
    for r in row_set:
        for c in range(n):
            A[r][c] = 0

    # change all cols with 0 to 0
    for c in col_set:
        for r in range(m):
            A[r][c] = 0


"""Another way without using sets."""


def set_zeroes(A):
    m, n, first_row_has_zero = len(A), len(A[0]), not all(A[0])

    for i in range(1, m):
        for j in range(n):
            if A[i][j] == 0:
                A[i][0] = A[0][j] = 0

    for i in range(1, m):
        for j in range(n - 1, -1, -1):
            if A[i][0] == 0 or A[0][j] == 0:
                A[i][j] = 0

    if first_row_has_zero:
        A[0] = [0] * n
