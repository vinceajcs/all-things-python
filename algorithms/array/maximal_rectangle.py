"""Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

The idea here is based on the solution to the largest rectangle in a histogram problem.
For each row in the matrix, we build a 'histogram' by calculating the height of each bar i.
This is done by finding the count of consecutive 1s from a row to above rows.

Then, we get the max rectangle for each bar like we do in the largest rectangle in a histogram problem.

Time: O(m*n)
Space: O(n)
"""


def max_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    heights = [0] * (n + 1)
    max_area = 0

    for row in matrix:
        # build histogram
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0

        # get max rectangle for each bar i
        stack = [-1]
        for i in range(n + 1):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

    return max_area
