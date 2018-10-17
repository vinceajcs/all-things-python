"""Idea: Use binary search.
If an element is smaller than its right neighbor, then there must be a peak element on its right because elements on its right is either:
1. always increasing -> rightmost element is peak
2. always decreasing -> leftmost element is peak
3. increase, then decrease -> pivot is peak
4. decrease, then increase -> leftmost element is peak

Thus we can find peak on the right side of the array. The same idea applies for the left side.

if n = 1, return nums[0]
if n = 2, return index of bigger number
else
    find mid, compare with left and right neighbors
    return mid if nums[mid] greater than left and right
    take right half if nums[mid] smaller than right neighbor
    else take left half

Time: O(logn)
Space: O(1)
"""


def find_peak(nums):
    if not nums:
        return -1

    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        peak = max(nums)
        return nums.index(peak)

    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            # found peak
            return mid
        elif nums[mid] < nums[mid + 1]:
            # search left half
            l = mid + 1
        else:
            # search right half
            r = mid - 1

    return l
