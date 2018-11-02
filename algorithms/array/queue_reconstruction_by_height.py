"""Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h.
Reconstruct the queue.

Idea:

1. Find the tallest group of people and sort them in a subarray.
Since there are no other groups taller than them, make person's index the same as their k-value.

2. For 2nd, 3rd...nth tallest group, insert each person into the subarray at the index = k-value.


Time: O(n**2)
Space: O(n)
"""


def reconstruct_queue(people):
    # sort by index
    people = sorted(people, key=lambda x: x[1])
    # sort by height, so that tallest people are at the front
    people = sorted(people, key=lambda x: x[0], reverse=True)

    result = []
    for p in people:
        k = p[1]
        result.insert(k, p)

    return result
