"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Idea: Use two pointers; similiar idea to two sum.

Time: O(n**2)
Space: O(1)
"""


def three_sum(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                # found a trio that when summed, is equal to 0
                result.append((nums[i], nums[l], nums[r]))

                # skip duplicates
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1

        return result
