"""Given a n by n matrix, rotate it by 90 degrees (clockwise).

Idea: Flip matrix upside down, then transpose the matrix.

Time: O(n**2)
Space: O(1)
"""


def rotate(A):
    A.reverse()
    # transpose matrix
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]


def rotate(A):
    # zip(*A) transposes the matrix A
    A[:] = zip(*A[::-1])


def rotate(A):
    # using list comprehension
    A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]
