"""Given a binary array, find the maximum number of consecutive 1s in the array.

Time: O(n)
Space: O(1)
"""


def max_consecutive_ones(nums):
    if not nums:
        return 0

    count = 0
    max_count = 0
    for n in nums:
        if n == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count
