"""Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

A positive number can be made with either two negatives, or two positives.
A positive and a negative number = a negative number, but this negative number can be later multiplied with another negative number to produce a positive.

Idea:
We keep track of both a local min and a local max.

If the current number, n, is >= 0, then:
    local_max = max(n, local_max * n)
    local_min = min(n, local_min * n)

If n is, however, negative:
    local_max = max(n, local_min * n)
    local_min = min(n, local_max * n)

The max product subarray is then the max of all the local maxes.

Time: O(n)
Space: O(1)
"""


def max_product(nums):
    max_product = local_max = local_min = nums[0]

    for n in nums[1:]:
        # pos * neg = neg, but neg * neg = pos, so we swap the extremums if the number is negative
        if n < 0:
            local_max, local_min = local_min, local_max

        local_max = max(n, local_max * n)
        local_min = min(n, local_min * n)

        max_product = max(max_product, local_max)

    return max_product
