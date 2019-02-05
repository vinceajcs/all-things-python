"""Given a list of points, find the k closest to the origin."""


from heapq import *
from random import randint


def distance(point, origin=(0, 0)):
    return point[0]**2 + point[1]**2


def naive(points, k, origin=(0, 0)):
    return sorted(points, key=lambda p: distance(p, origin))[:k]


"""Better solution.

Idea: Maintain a max heap of k elements.
We can iterate through all points.
If a point p has a smaller distance to the origin than the top element of a heap, we add point p to the heap and remove the top element.
After iterating through all points, our heap contains the k closest points to the origin.

Time: O(nlogk)
Space: O(k)
"""


def k_closest(points, k, origin=(0, 0)):
    """Initialize max heap with first k points.
    Python does not support a max heap; thus we can use the default min heap where the keys (distance) are negated.
    """
    heap = [(-distance(p, origin), p) for p in points[:k]]
    heapify(heap)

    """
    For every point p in points[k:],
    check if p is smaller than the root of the max heap;
    if it is, add p to heap and remove root. Reheapify.
    """
    for p in points[k:]:
        d = distance(p, origin)

        heappushpop(heap, (-d, p))  # heappushpop does conditional check
        """Same as:
            if d < -heap[0][0]:
                heappush(heap, (-d,p))
                heappop(heap)

        Note: heappushpop is more efficient than separate push and pop calls.
        Each heappushpop call takes O(logk) time.
        """

    return [p for nd, p in heap]  # return points in heap


"""Another idea: find kth element, and return all elements less than that element.
This can be done in linear time, using quickselect.
"""
