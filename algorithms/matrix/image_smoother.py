"""Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

Time: O(m*n)
Space: O(m*n)
"""


def image_smoother(matrix):
    if not matrix:
        return matrix

    m, n = len(matrix), len(matrix[0])

    result = [[0] * n for _ in range(m)]

    directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    for i in range(m):
        for j in range(n):
            count = 0
            neighbors = 0

            for direction in directions:
                x, y = i + direction[0], j + direction[1]

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                count += matrix[x][y]
                neighbors += 1

            result[i][j] = count // neighbors

    return result
