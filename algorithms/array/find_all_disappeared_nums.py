"""Given an array of integers where 1 ≤ a[i] ≤ n, some elements appear twice and others appear once.
Find all the elements of 1...n inclusive that do not appear in this array.

Time: O(n)
Space: O(1)
"""


def find_disappeared_nums(nums):
    whole_set = set([x for x in range(1, len(nums) + 1)])
    missing = whole_set.difference(set(nums))
    return list(missing)


"""Another way."""


def find_disappeared_nums(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])

    return [i for i, n in enumerate(nums, start=1) if n > 0]
