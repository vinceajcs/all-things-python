"""Same problem as jump game, but this time return the minimum number of jumps.

We can use two pointers, left and right.
Initially, left = 0 and right = nums[0].
Indices between left and right are indices reachable in a jump.
So, indices 0 to nums[0] are the indices you can reach initially.
For the second jump and onwards, left = right, and right will be equal to the farthest reachable index with x jumps.

Time: O(n)
Space: O(1)
"""


def min_jumps(nums):
    if len(nums) <= 1:
        return 0

    l, r = 0, nums[0]
    count = 1

    while r < len(nums) - 1:
        count += 1
        next_right = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, next_right

    return count
