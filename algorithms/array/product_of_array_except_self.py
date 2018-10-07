"""Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Idea:
output[i] = product of nums left of i * product of nums right of i

For the example above,
output = [
left: 1         nums[i] = 1 right: 2 * 3 * 4 // 2 * 3 * 4 = 24
left: 1         nums[i] = 2 right: 3 * 4     // 1 * 3 * 4 = 12
left: 1 * 2     nums[i] = 3 right: 4         // 1 * 2 * 4 = 8
left: 1 * 2 * 3 nums[i] = 4 right: init 1    // 1 * 2 * 3 = 6
]

Thus, we can solve this by iterating through the array twice (left, then right).

Time: O(n)
Space: O(1)
"""


def product(nums):
    output = []
    n = len(nums)

    p = 1
    # left pass
    for i in range(n):
        output.append(p)
        p *= nums[i]

    p = 1
    # right pass
    for i in range(n - 1, -1, -1):
        output[i] *= p
        p *= nums[i]

    return output
