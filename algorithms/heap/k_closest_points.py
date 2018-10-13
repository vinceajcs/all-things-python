"""Given a list of points, find the k closest to the origin."""


from heapq import *
from random import randint


def distance(point, origin=(0, 0)):
    return point[0]**2 + point[1]**2


def naive(points, k, origin=(0, 0)):
    return sorted(points, key=lambda p: distance(p, origin))[:k]


"""Better solution: the idea here is to maintain a max heap with the k closest points.

Time: O(nlogk)
Space: O(k)
"""


def closest(points, k, origin=(0, 0)):
    """Create max heap with first k points.
    Python does not support a max heap; thus we can use a min heap where the keys are negated
    """
    heap = [(-distance(p, origin), p) for p in points[:k]]
    heapify(heap)

    """
    For every point p in points[k:],
    check if p is smaller than the root of the max heap;
    if it is, remove root and add p to heap. Reheapify.
    """
    for p in points[k:]:
        d = distance(p, origin)

        heappushpop(heap, (-d, p))  # heappushpop does conditional check
        """same as:
            if d < -heap[0][0]:
                heappush(heap, (-d,p))
                heappop(heap)
        """

    return [p for nd, p in heap]  # return points in heap


"""Another idea: find kth element, and return all elements less than that element.
This can be done in linear time, using quickselect."""
