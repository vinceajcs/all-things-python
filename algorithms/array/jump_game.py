"""Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

We can iterate through the array from left to right and keep track of the furthest reachable index at each step.
For an index to be reachable, each of the previous indices have to be reachable.

Time: O(n)
Space: O(1)
"""


def can_jump(nums):
    max_reachable = 0

    for i, n in enumerate(nums):
        if i > max_reachable:  # index i is not reachable
            return False
        max_reachable = max(max_reachable, i + n)

    return True  # all indices are reachable since loop finished


"""Going backwards."""


def can_jump(nums):
    goal = len(nums) - 1

    for i in range(len(nums))[::-1]:
        if i + nums[i] >= goal:
            goal = i

    return not goal
