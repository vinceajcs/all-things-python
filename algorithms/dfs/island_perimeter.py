"""Given a 2D grid and exactly one island, find the perimeter of the island.

Time: O(m*n)
Space: O(1)
"""


def island_perimeter(grid):
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    perimeter = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += dfs(grid, i, j, m, n)

    return perimeter


def dfs(grid, i, j, m, n):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    result = 0
    for direction in directions:
        x, y = i + direction[0], j + direction[1]

        if x < 0 or x == m or y < 0 or y == n or grid[x][y] == 0:
            result += 1

    return result
