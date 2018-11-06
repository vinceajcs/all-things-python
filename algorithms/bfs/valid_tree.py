"""Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), check whether these edges make up a valid tree.

Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

A tree is connected, acyclic, and contains n-1 edges, where n is the number of nodes.
We can use BFS to check if there's a cycle and only one connected component in the graph.

Time: O(m+n)
Space: O(m+n)
"""


def valid_tree(n, edges):
    lookup = {i: set() for i in range(n)}  # n nodes from 0 to n-1

    # create graph
    for x, y in edges:
        lookup[x].add(y)
        lookup[y].add(x)

    visited = set()
    queue = collections.deque([list(lookup.keys())[0]])

    while queue:
        node = queue.popleft()

        if node in visited:  # cycle
            return False

        visited.add(node)

        for neighbour in lookup[node]:
            queue.append(neighbour)
            lookup[neighbour].remove(node)

        lookup.pop(node)

    return not lookup  # if there are any nodes left, that means there is more than one connected component
