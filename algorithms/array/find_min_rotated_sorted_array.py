"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(e.x., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example:
Input: [3,4,5,1,2]
Output: 1

Idea: Use binary search.

Time: O(logn)
Space: O(1)
"""


def find_min(nums):
    if not nums:
        return

    if len(nums) == 1:
        return nums[0]

    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # second half of array is not in sorted order
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]


"""Same problem as above, but this time with duplicates."""


def find_min(nums):
    if not nums:
        return

    if len(nums) == 1:
        return nums[0]

    low, high = 0, len(nums) - 1

    # remove duplicates
    while nums[low] == nums[high] and low < high:
        high -= 1

    while low < high:
        mid = (low + high) // 2

        # second half of array is not in sorted order
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]
