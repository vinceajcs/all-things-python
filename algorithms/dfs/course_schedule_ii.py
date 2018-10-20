"""Same as course schedule, but this time we need to output an ordering of the courses.
We can accomplish this to topologically sort the DAG to return a topological ordering of the courses.

Time: O(m+n)
Space: O(n)
"""


def find_order(n, prereqs):
    graph = collections.defaultdict(list)
    topological_order = []

    for pair in prereqs:
        graph[pair[0]].append(pair[1])  # pair[0] is a node, pair[1] is its neighbor

    visited = [0] * n

    for node in range(n):
        if not dfs(graph, visited, topological_order, node):
            return []

    return topological_order


def dfs(graph, visited, order, node):
    # check for cycle
    if visited[node] == -1:
        return False

    if visited[node] == 1:
        return True

    visited[node] = -1  # mark as visited in a current run

    # visit neighbors of node
    for j in graph[node]:
        if not dfs(graph, visited, order, j):
            return False

    visited[node] = 1
    order.append(node)

    return True
