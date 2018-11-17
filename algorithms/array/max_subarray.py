"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Time: O(n)
Space: O(1)
"""


def max_subarray(nums):
    # use each index to represent the max subarray ending with that index
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


def max_subarray(nums):
    # similar approach as above
    cur_sum = max_sum = nums[0]

    for n in nums[1:]:
        if cur_sum > 0:
            cur_sum += n
        else:
            cur_sum = n
        max_sum = max(max_sum, cur_sum)

    return max_sum


"""Use Kadane's algorithm.

Idea: The max subarray sum ending at index i either:
(1) contains the element at index i
(2) contains the subarray that ends at position i-1, followed by the element at index i
"""


def max_subarray(nums):
    cur_sum = max_sum = nums[0]

    for n in nums[1:]:
        cur_sum = max(n, cur_sum + n)
        max_sum = max(max_sum, cur_sum)

    return max_sum
