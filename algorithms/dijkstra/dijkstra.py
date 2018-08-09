import heapq


def dijkstra(graph, source):
    d = {v: float('inf') for v in graph}
    d[source] = 0
    pq = []

    for v, dist in d.items():
        heapq.heappush(pq, [dist, v])

    while pq:
        u_dist, u = heapq.heappop(pq)
        for v, uv_dist in graph[u].items():
            dist = d[u] + uv_dist
            if dist < d[v]:
                d[v] = dist
                heapq.heappush(pq, [dist, v])

    return d


graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

graph2 = {'a': {'b': 14, 'c': 9, 'd': 7},
          'b': {'a': 14, 'c': 2, 'e': 9},
          'c': {'a': 9, 'b': 2, 'd': 10, 'f': 11},
          'd': {'a': 7, 'c': 10, 'f': 15},
          'e': {'b': 9, 'f': 6},
          'f': {'c': 11, 'd': 15, 'e': 6}}


print(dijkstra(graph2, 'a'))
