"""Given an m by n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific Ocean" touches the left and top edges of the matrix and the "Atlantic Ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Idea: Iterate through entire matrix.
1. At each cell, traverse through all its neighbors to see if the neighbor has a height equal or less than that of itself.
2. Maintain 2 boolean matrices, for the 2 oceans. Mark a cell x, y true if it can reach the specified ocean.
3. Finally, iterate through all cells to see if the coordinate can reach both oceans.

Time: O(m*n)
Space: O(m*n)
"""


def pacific_atlantic(matrix):
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])

    pacific = [[False for _ in range(n)] for _ in range(m)]
    atlantic = [[False for _ in range(n)] for _ in range(m)]

    result = []  # list of cells that can flow to both pacific and atlantic

    for i in range(m):
        dfs(matrix, pacific, atlantic, i, 0, m, n)
        dfs(matrix, pacific, atlantic, i, n - 1, m, n)

    for j in range(n):
        dfs(matrix, pacific, atlantic, 0, j, m, n)
        dfs(matrix, pacific, atlantic, m - 1, j, m, n)

    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])

    return result


def dfs(matrix, visited, i, j, m, n):
    visited[i][j] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        x, y = i + direction[0], j + direction[1]

        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
            continue

        dfs(matrix, visited, x, y, m, n)
