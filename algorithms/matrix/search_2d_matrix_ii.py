"""Search for a value in an m by n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending order from left to right.
Integers in each column are sorted in ascending order from top to bottom.

Example:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


Idea:
1. Start with top right element
2. If target < top right element, then target cannot be in that column
Thus, we go a column to the left (decrease column)
3. If target > matrix[0][col-2], then we go down a row (increase row)


Time: O(m+n)
Space: O(1)
"""


def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False
