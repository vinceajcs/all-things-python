"""Given an integer array with all positive numbers and no duplicates, find the number of possible permutations that add up to a positive integer target.

We can define cc(i) = number of permutations that sum to i.

cc(i) = 0 if i < 0
        1 if i = 0 (only 1 way to form empty sum)
        cc(i) += cc(i-c), for c in coins, o.w.

Time: O(t*n), where t = target
Space: O(t)
"""


def combination_sum(nums, target):
    cc = [0 for _ in range(target + 1)]
    cc[0] = 1

    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                cc[i] += cc[i - num]

    return cc[-1]
