"""Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down.

Time: O(m*n)
Space: O(m*n)
"""


def longest_increasing_path(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    cache = [[-1 for _ in range(n)] for _ in range(m)]

    longest_path = 0

    for i in range(m):
        for j in range(n):
            current_length = dfs(matrix, cache, i, j, m, n)
            longest_path = max(longest_path, current_length)

    return longest_path


def dfs(matrix, cache, i, j, m, n):
    # already visited
    if cache[i][j] != -1:
        return cache[i][j]

    longest_path = 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        x, y = i + direction[0], j + direction[1]
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
            continue

        path = 1 + dfs(matrix, cache, x, y, m, n)
        longest_path = max(longest_path, path)

    cache[i][j] = longest_path
    return longest_path
