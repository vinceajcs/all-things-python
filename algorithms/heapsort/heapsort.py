def heapsort(iterable):
    """Note: Heapsort is not stable. The relative order of equal elements can change."""
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]
