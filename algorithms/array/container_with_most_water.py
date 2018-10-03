"""Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Idea: Use two pointers.
Start with widest container (good candidate for max area). Use left and right pointers to point to start and end of array.
All other possible containers would be less wide, so we would need a higher water level for greater area.
For each iteration, advance the pointer of the shorter line, since height of area will always be the shorter/smaller of the 2 lines.

Time: O(n)
Space: O(1)
"""


def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        cur_width = right - left
        # area is determined by the shorter of the two heights
        cur_area = cur_width * min(heights[left], heights[right])
        # update max area
        max_area = max(max_area, cur_area)

        # advance index of shorter height / shorter line
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area
