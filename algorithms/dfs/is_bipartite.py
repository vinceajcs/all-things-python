"""Determine if an undirected graph is bipartite.
A graph is bipartite if we can split its set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

Idea: Color the graph with 2 colors.
For each uncolored node, start coloring process with DFS.
If two neighbor nodes have the same color, graph is not bipartite.

Time: O(m+n)
Space: O(n)
"""


def is_bipartite(graph):
    color = {}  # stores color of each node

    for node in range(len(graph)):
        if node not in color:
            stack = [node]
            color[node] = 0

            while stack:
                node = stack.pop()

                for neighbor in graph[node]:
                    if neighbor not in color:
                        stack.append(neighbor)
                        color[neighbor] = color[node] ^ 1
                    elif color[neighbor] == color[node]:
                        return False
    return True
