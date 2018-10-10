"""Given an array of integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

Example:
nums = [-1, 2, 1, -4], target = 1
The sum that is closest to the target is 2 (-1 + 2 + 1 = 2).

Time: O(n**2)
Space: O(1)
"""


def three_sum_closest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1

        while l < r:
            sum = nums[i] + nums[l] + nums[r]

            if sum == target:
                return sum

            # compare current sum and closest sum so far
            if abs(sum - target) < abs(result - target):
                result = sum

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1

    return result
