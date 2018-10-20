"""Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Idea: Iterate through each cell in the matrix, and if it is an island, traverse its neighbors to mark adjacent islands.

Time: O(m*n)
Space: O(m*n)
"""


def islands(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    islands = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dfs(matrix, i, j, m, n)
                islands += 1

    return islands


def dfs(matrix, i, j, m, n):
    matrix[i][j] = '0'
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for direction in directions:
        x, y = i + direction[0], j + direction[1]
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] != '1':
            continue
        dfs(matrix, x, y, m, n)
