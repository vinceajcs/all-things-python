"""Same problem as unique paths, but this time there are obstacles (1s) in the grid.

Idea: We can set all obstacles we encounter (1s) to 0s in our dp table when we traverse the grid.

Time: O(m*n)
Space: O(m*n)
"""


def unique_paths(grid):
    m, n = len(grid), len(grid[0])

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    dp[0][1] = 1  # start from cell (0, 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if not grid[i - 1][j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]


"""Again, we can optimize space."""


def unique_paths(grid):
    m, n = len(grid), len(grid[0])

    dp = [0 for _ in range(n)]

    dp[0] = 1

    for row in grid:
        for j in range(n):
            if row[j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]

    return dp[n - 1]
