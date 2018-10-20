"""Same as house robber, but this time first and last houses are adjacent."""


def house_robber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    # solution either includes first or last house, but cannot include both
    return max(helper(nums[1:]), helper(nums[:-1]))


def helper(self, nums):
    dp = [0] * len(nums)

    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

    return dp[-1]
