"""There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

We can use DFS to detect a cycle in a graph of courses (check for back edges).

Time: O(m+n)
Space: O(n)
"""


def can_finish(courses, prereqs):
    graph = [[] for _ in range(courses)]
    visited = [0 for _ in range(courses)]  # same as [0] * courses

    # create graph
    for pair in prereqs:
        x, y, = pair  # x is a node, y is its neighbor
        graph[x].append(y)

    # visit each node in graph
    for i in range(courses):
        if not dfs(graph, visited, i):
            return False

    return True


def dfs(graph, visited, i):
    # check if there's a cycle
    if visited[i] == -1:
        return False

    # if it has already been visited in a current run, do not visit again
    if visited[i] == 1:
        return True

    visited[i] = -1  # mark as visited in a current run

    # visit neighbors
    for j in graph[i]:
        if not dfs(graph, visited, j):
            return False

    visited[i] = 1  # after visiting all neighbors, mark the finish of a current run
    return True
