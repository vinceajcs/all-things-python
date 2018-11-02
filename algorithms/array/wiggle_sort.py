"""Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Time: O(n)
Space: O(1)
"""


"""Sort nums, and then swap by pairs."""


def wiggle_sort(nums):
    nums.sort()  # sorting bottleneck O(nlogn)

    n = len(nums) if len(nums) % 2 == 0 else len(nums) - 1

    for i in range(2, n, 2):
        nums[i - 1], nums[i] = nums[i], nums[i - 1]


"""Better idea using one pass through the array."""


def wiggle_sort(nums):
    for i in range(len(nums) - 1):
        if i % 2 == 0:  # even index
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:  # odd index
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
