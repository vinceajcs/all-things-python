"""Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), find the number of connected components in an undirected graph.


Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4
Output: 2

Example 2:
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3
Output: 1

Assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

We can traverse the graph with DFS.

Time: O(m+n)
Space: O(n)
"""


def connected_components(n, edges):
    def dfs(node, graph, visited):
        if visited[node]:
            return
        visited[node] = 1
        for neighbor in graph[node]:
            dfs(neighbor, graph, visited)

    visited = [0] * n
    graph = collections.defaultdict(list)

    # create graph
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    count = 0

    for node in range(n):
        if not visited[node]:
            dfs(node, graph, visited)
            count += 1

    return count
