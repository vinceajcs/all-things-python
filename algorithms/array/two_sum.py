"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Time: O(n)
Space: O(n)
"""


def two_sum(nums, target):
    lookup = {}

    for index, num in enumerate(nums):
        difference = target - num
        if difference in lookup:
            return lookup[difference], index
        else:
            lookup[num] = index


"""Same problem, but this time the input array is sorted. Here, we can solve this using two pointers."""


def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return l, r  # return nums[l], nums[r] to return actual numbers instead of indices
        elif s < target:
            l += 1
        else:
            r -= 1
