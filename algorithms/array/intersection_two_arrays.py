"""Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.

Time: O(len(nums1) + len(nums2))
Space: O(len(nums1) + len(nums2))
"""


def intersection(nums1, nums2):
    set1 = set(nums1)  # O(len(nums1))
    set2 = set(nums2)  # O(len(nums2))

    return list(set1.intersection(set2))  # O(min(len(nums1), len(nums2)))
