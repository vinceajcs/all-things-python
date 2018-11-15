"""Given a DAG, return a topological ordering of its nodes."""


def topological_sort(graph):
    visited = collections.defaultdict(bool)

    stack = []

    for node in graph.keys():
        if not visited[node]:
            dfs(graph, node, visited, stack)

    return stack  # stack should contain the topological order of the nodes in the DAG


def dfs(graph, node, visited, stack):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)

    stack.insert(0, node)
