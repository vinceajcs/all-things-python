"""Given a matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2)."""


class RangeSum2DMatrix:
    def __init__(self, matrix):
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col - 1]

        self.matrix = matrix

    def update(self, row, col, val):  # O(n)
        original = self.matrix[row][col]

        if col != 0:
            original -= self.matrix[row][col - 1]

        diff = original - val

        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sum_region(self, row1, col1, row2, col2):  # O(m)
        sum = 0
        for x in range(row1, row2 + 1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1 - 1]
        return sum


"""Using a 2D Binary Indexed Tree (https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/)."""


class RangeSum2DMatrix:
    def __init__(self, matrix):
        if not matrix:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * (self.n) for _ in range(self.m)]
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val

        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sum_region(self, row1, col1, row2, col2):
        return self.sum(row2, col2)
        + self.sum(row1 - 1, col1 - 1)
        - self.sum(row1 - 1, col2)
        - self.sum(row2, col1 - 1)

    def sum(self, row, col):
        result = 0

        i = row + 1
        while i:
            j = col + 1
            while j:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)

        return result
