"""Given a list of distinct integers, nums, return all possible subsets, otherwise known as the power set.

Time: O(2**n)
Space: O(1)
"""


# recursive
def subsets(nums):
    power_set = []
    backtrack(sorted(nums), 0, [], power_set)
    return power_set


def backtrack(nums, index, path, result):
    result.append(path)
    for i in range(index, len(nums)):
        backtrack(nums, i + 1, path + [nums[i]], result)


# iterative
def subsets(S):
    power_set = [[]]
    for e in S:
        power_set += [x + [e] for x in power_set]
    return power_set
