"""We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array, find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Time: O(n)
Space: O(n)
"""


def longest_harmonious_subsequence(nums):
    if not nums:
        return 0

    # create dict of char -> freq
    # same as Counter(nums)
    lookup = {}
    for num in nums:
        if num not in lookup:
            lookup[num] = 1
        else:
            lookup[num] += 1

    max_length = 0

    # for each num, check if num+1 is also in nums
    # if it is, the length of the LHS is freq of num + freq of num+1
    for num in lookup:
        if num + 1 in lookup:
            max_length = max(max_length, lookup[num] + lookup[num + 1])

    return max_length
