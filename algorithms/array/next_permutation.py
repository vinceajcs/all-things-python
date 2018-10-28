"""Given a list of numbers, rearrange the list into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, rearrange the list into the lowest possible order (i.e., sorted in ascending order).

Idea: increase the sequence as little as possible.
To do so, we can:
1. Find longest non-increasing suffix
2. Identify a pivot (index where suffix is no longer non-increasing)
If such a pivot does not exist, list is sorted in descending order. So just reverse the list to get lowest possible order.
3. If we find a pivot, we have to find the smallest element in the suffix that is greater than pivot.
We swap this smallest element that is greater than the pivot with the pivot. This is done to minimize the prefix.
4. Finally, we sort the suffix in non-decreasing order.

Time: O(n)
Space: O(1)
"""


def next_permutation(nums):
    """Modify nums in-place."""

    # find the longest non-increasing suffix and get pivot (nums[i-1])
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1

    if i <= 0:  # list is already sorted in descending order
        nums[:] = nums[::-1]  # so, we just reverse the list to get lowest possible order
        return

    # find smallest element in suffix that is greater than pivot (nums[i-1])
    j = len(nums) - 1
    while j > 0 and nums[j] <= nums[i - 1]:
        j -= 1

    # swap pivot with smallest element in suffix that is greater than pivot
    nums[i - 1], nums[j] = nums[j], nums[i - 1]

    # sort suffix in non-decreasing order (we can accomplish this by reversing the suffix)
    nums[:] = nums[:i] + nums[i:len(nums)][::-1]
