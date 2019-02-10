"""You are asked to cut off trees in a forest for a golf event.
The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first.
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees.
If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6

Example 2:
Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1

Example 3:
Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.

Time: O((m*n)^2)
Space: O(m*n)
"""


def cut_off_trees(forest):
    if not forest:
        return 0

    m, n = len(forest), len(forest[0])

    # add all trees and their locations to the heap
    heap = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
    heapq.heapify(heap)

    steps = 0
    row, col = 0, 0

    while heap:
        height, tree_row, tree_col = heapq.heappop(heap)
        dist = get_distance(forest, row, col, tree_row, tree_col, m, n)

        if dist == -1:
            return -1

        forest[tree_row][tree_col] = 1
        steps += dist
        row, col = tree_row, tree_col

    return steps


def get_distance(forest, start_row, start_col, tree_row, tree_col, m, n):
    dist = 0
    queue = collections.deque([(start_row, start_col)])
    visited = set((start_row, start_col))

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            if row == tree_row and col == tree_col:
                return dist

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for direction in directions:
                next_row, next_col = row + direction[0], col + direction[1]
                if (0 <= next_row < m and 0 <= next_col < n and
                        (next_row, next_col) not in visited and forest[next_row][next_col]):
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col))

        dist += 1

    return -1
