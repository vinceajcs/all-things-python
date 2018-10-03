"""Given a m by n matrix, return all elements of the matrix in spiral order.

Time: O(m*n)
Space: O(1)
"""


def spiral_order(A):
    result = []

    if not A:
        return result

    left, right, top, bottom = 0, len(A[0]) - 1, 0, len(A) - 1

    while left <= right and top <= bottom:
        # go from left to right, starting from leftmost column
        for j in range(left, right + 1):
            result.append(A[top][j])

        # top to bottom, starting from first row
        for i in range(top + 1, bottom):
            result.append(A[i][right])

        # right to left, starting from rightmost column
        for j in reversed(range(left, right + 1)):
            if top < bottom:
                result.append(A[bottom][j])

        # bottom to top, starting from last row
        for i in reversed(range(top + 1, bottom)):
            if left < right:
                result.append(A[i][left])

        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

    return result


"""Another idea:
1. Extract first row from matrix and add to result list
2. Transpose the matrix, then flip it upside down (same as reversing it)
3. Repeat while matrix is not empty
"""


def spiral_order(A):
    result = []
    while A:
        first_row = A.pop(0)
        result.extend(first_row)
        # zip(*A) transposes matrix A
        A = [*zip(*A)][::-1]
    return result
