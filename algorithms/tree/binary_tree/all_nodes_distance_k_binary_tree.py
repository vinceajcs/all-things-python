"""We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.

We can convert the tree into a regular graph (adjacency list) using DFS, then use BFS from the target node to get nodes k distances away.

Time: O(n)
Space: O(n)
"""


def nodes_distance_k(root, target, k):
    graph = collections.defaultdict(list)

    def dfs(parent, child):
        if parent and child:
            graph[parent.val].append(child.val)
            graph[child.val].append(parent.val)

        if child.left:
            dfs(child, child.left)
        if child.right:
            dfs(child, child.right)

    # create graph from tree
    dfs(None, root)

    # bfs/level order traversal from target node
    level = [target.val]
    visited = set(level)

    for _ in range(k):
        next_level = []
        for node in level:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    next_level.append(neighbor)
                    visited.add(neighbor)
        level = next_level

    return level
