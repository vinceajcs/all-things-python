"""Given a unsorted array of integers, find the longest increasing subarray.

Time: O(n)
Space: O(1)
"""


def longest_increasing_subarray(nums):
    if not nums:
        return 0

    max_length, i = 0, 0

    while i < len(nums):
        curr_length = 1
        while (i + 1) < len(nums) and nums[i] < nums[i + 1]:  # extend streak if possible
            curr_length += 1
            i += 1

        max_length = max(max_length, curr_length)  # update max length
        i += 1

    return max_length
