"""Return the kth row in pascal's triangle."""


def pascal_triangle(row_index):
    pascal = [[1] * (i + 1) for i in range(row_index + 1)]
    for i in range(row_index + 1):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal[-1]


"""Another way, using less space."""


def pascal_triangle(row_index):
    row = [1]
    for i in range(row_index):
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
    return row
