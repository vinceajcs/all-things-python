"""Search for a value in an m by n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

We can use binary search.

Time: O(logn)
Space: O(1)
"""


def search_matrix(matrix, target):
    flattened = [x for row in matrix for x in row]

    l, r = 0, len(flattened) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == flattened[mid]:
            return True
        elif target > flattened[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return False


"""Without using extra space."""


def search_matrix(matrix, target):
    if not matrix:
        return False

    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1

    while low <= high:
        mid = (low + high) // 2

        num = matrix[mid // n][mid % n]
        if target == num:
            return True
        elif target > num:
            low = mid + 1
        else:
            high = mid - 1

    return False
