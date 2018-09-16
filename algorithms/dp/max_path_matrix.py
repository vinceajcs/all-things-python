def max_path(grid):

    m, n = len(grid), len(grid[0])

    max_path = [[0 for _ in range(n)] for _ in range(m)]

    max_path[0][0] = grid[0][0]

    for i in range(1, m):
        max_path[i][0] = max_path[i - 1][0] + grid[i][0]
    for j in range(1, n):
        max_path[0][j] = max_path[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            # for min path, just change max to min
            max_path[i][j] = max(max_path[i][j - 1], max_path[i - 1][j]) + grid[i][j]

    return max_path[-1][-1]


test = [[3, 7, 9, 2, 7],
        [9, 8, 3, 5, 5],
        [1, 7, 9, 8, 5],
        [3, 8, 6, 4, 10],
        [6, 3, 9, 7, 8]]

print(max_path(test))  # should equal 67
