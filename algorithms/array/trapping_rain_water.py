"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Idea: Use two pointers, one left and one right.
For each iteration,
    1. Choose which pointer to move based on which side has greater height.
    (If there is a greater height at one end (for example, right), then water trapped is dependent on height of bar in current direction (left to right))
    2. Add water

Time: O(n)
Space: O(1)
"""


def trap_water(heights):
    l, r = 0, len(heights) - 1
    left_max, right_max = 0, 0
    water = 0

    while l < r:
        if heights[l] > left_max:
            left_max = heights[l]

        if heights[r] > right_max:
            right_max = heights[r]

        # decide which pointer to move based on height of both sides
        if left_max < right_max:
            # water = current max height - current height
            water += left_max - heights[l]
            l += 1
        else:
            water += right_max - heights[r]
            r -= 1

    return water
