"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(e.x., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Idea: Use binary search.

Time: O(logn)
Space: O(1)
"""


def search(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid

        # check if first half of array is still in sorted order
        if nums[low] <= nums[mid]:
            # check if target is in first half of array
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            # check if target is in second half of array
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


"""Same problem as above, but return True/False instead of an index."""


def search(nums, target):
    if not nums:
        return False

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return True

        while low < mid and nums[low] == nums[mid]:  # tricky part
            low += 1

        # check if first half of array is still in sorted order
        if nums[low] <= nums[mid]:
            # check if target is in first half of array
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            # check if target is in second half of array
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False
