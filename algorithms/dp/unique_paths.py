"""Given a m by n matrix, determine the number of unique paths from the top left cell to the bottom right cell.

Time: O(m*n)
Space: O(m*n)
"""


def unique_paths(grid):
    m, n = len(grid), len(grid[0])

    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[-1][-1]


"""We can optimize space since we only need top and left cells to calculate a given cell.
Thus we can just maintain two columns (current and left), instead of the entire matrix.
"""


def unique_paths(grid):
    m, n = len(grid), len(grid[0])

    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j - 1] + dp[j]

    return dp[-1]
