"""Design a Tic-Tac-Toe game that is played between two players on a n x n grid.

Idea:
Record the number of moves for each rows, columns, and two diagonals.
For each move, we -1 for each player 1's move and +1 for player 2's move.
Then we just need to check whether any of the recorded numbers equal to n or -n.
"""


class TicTacToe:
    def __init__(self, n):
        self.row, self.col = [0] * n, [0] * n
        self.diag, self.anti_diag = 0, 0
        self.n = n

    def move(self, row, col, player):
        offset = player * 2 - 3

        self.row[row] += offset
        self.col[col] += offset

        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset

        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:  # player 2 wins
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:  # player 1 wins
            return 1

        return 0  # no one has won yet
