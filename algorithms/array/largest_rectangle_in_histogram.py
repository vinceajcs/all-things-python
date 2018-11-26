"""Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Idea: For any bar i, the max rectangle has a width of r-l-1, where l is the first coordinate to the left of the bar i with height h[l] < h[i].
Similarly, r is the first coordinate to the right of the bar i with height h[r] < h[i].
We can then find all r, l, and then calculate the max rectangle that can be formed at each bar i.
We return the max rectangle of them all.

Time: O(n)
Space: O(n)
"""


def largest_rectangle(heights):
    if not heights:
        return 0

    n = len(heights)

    shorter_lefts = [0] * n  # indices of first bar to the left that is shorter than current bar i
    shorter_rights = [0] * n  # indices of first bar to the right that is shorter than current bar i

    shorter_lefts[0] = -1
    shorter_rights[n - 1] = n

    # get shorter left bars for each bar i
    for i in range(1, n):
        j = i - 1

        while j >= 0 and heights[j] >= heights[i]:
            j -= 1  # change this line to j = shorter_lefts[j] for O(n)

        shorter_lefts[i] = j

    # get shorter right bars for each bar i
    for i in range(n - 2, -1, -1):
        j = i + 1

        while j < n and heights[j] >= heights[i]:
            j += 1  # change this line to j = shorter_rights[j] for O(n)

        shorter_rights[i] = j

    # calculate max rectangles for each bar i and find the maximum
    max_area = 0
    for i in range(n):
        max_area = max(max_area, heights[i] * (shorter_rights[i] - shorter_lefts[i] - 1))

    return max_area


"""Using a stack.

Idea: For any bar i, if it's in a rectangle of which the height is also the height of i, we know that every bar in the rectangle must be no shorter than i.
Then the issue is to find the left and right boundary where the bars are shorter than i.
When a bar is popped out from the stack, we know it must be higher than the bar at position i, so bar[i] must be the right boundary (exclusive) of the rectangle,
and the previous bar in the stack is the first one that is shorter than the popped one so it must be the left boundary (also exclusive). Then we find the rectangle.
"""


def largest_rectangle(heights):
    heights.append(0)
    stack = [-1]
    max_area = 0

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            # current bar i is the left boundary l, stack[-1] is the right boundary r
            width = i - stack[-1] - 1
            max_area = max(ans, height * width)
        stack.append(i)

    heights.pop()  # restore heights to original state (optional in this context)
    return max_area
