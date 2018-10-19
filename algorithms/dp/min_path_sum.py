"""Given a m by n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

We can define sum(i, j) = min sum on a path from upper-left corner to cell (i, j).
As a result sum(m, n) tells us the min path sum from the upper left cell to lower right cell.

A path that ends at cell (i, j) can either come from either (i, j-1) or (i-1, j).
Thus,

sum(i, j) = 0 if i = 0 or j = 0
            min(sum(i, j-1), sum(i-1, j)) + grid(i, j) o.w.

Time: O(m*n)
Space: O(m*n)
"""


def min_path_sum(grid):
    m, n = len(grid), len(grid[0])

    min_path = [[0 for _ in range(n)] for _ in range(m)]

    min_path[0][0] = grid[0][0]

    for i in range(1, m):
        min_path[i][0] = min_path[i - 1][0] + grid[i][0]
    for j in range(1, n):
        min_path[0][j] = min_path[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            min_path[i][j] = min(min_path[i][j - 1], min_path[i - 1][j]) + grid[i][j]

    return min_path[-1][-1]
