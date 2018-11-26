"""Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Time: O(n)
Space: O(n)
"""


def intersection(nums1, nums2):
    result = []

    counter = collections.Counter(nums1)

    for num in nums2:
        if num in counter.keys():
            result.append(num)
            counter[num] -= 1

        if counter[num] == 0:
            del counter[num]

    return result


"""Sorting both arrays."""


def intersection(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    pt1 = pt2 = 0
    result = []

    while pt1 < len(nums1) and pt2 < len(nums2):
        if nums1[pt1] > nums2[pt2]:
            pt2 += 1
        elif nums1[pt1] < nums2[pt2]:
            pt1 += 1
        else:
            result.append(nums1[pt1])
            pt1 += 1
            pt2 += 1

    return result
