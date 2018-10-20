"""Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Time: O(m*n)
Space: O(1)
"""


def exist(board, word):
    if not board:
        return False

    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            # if first characters match
            if board[i][j] == word[0]:
                if dfs(board, word[1:], i, j, m, n):
                    return True

    return False


def dfs(board, word, i, j, m, n):
    if len(word) == 0:
        return True

    # mark character so it cannot be reused in the same traversal
    temp, board[i][j] = board[i][j], '#'

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        x, y = i + direction[0], j + direction[1]

        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[0]:
            continue

        if dfs(board, word[1:], x, y, m, n):
            return True

    # restore board
    board[i][j] = temp
    return False
