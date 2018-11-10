"""Given a non-negative integer rows, generate the first rows of Pascal's triangle.

Time: O(n**2)
Space: O(n**2)
"""


def pascal_triangle(rows):
    pascal = [[1] * (i + 1) for i in range(rows)]
    for i in range(rows):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal
