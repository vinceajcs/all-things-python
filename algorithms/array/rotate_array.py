"""Given an array, rotate the array to the right by k, where k is non-negative.

Time: O(n)
Space: O(1)
"""


def rotate(nums, k):
    n = len(nums) - k
    nums[:] = nums[n:] + nums[:n]


"""Reversing 3 times."""


def rotate(nums, k):
    n = len(nums)
    k = k % n

    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)


def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
