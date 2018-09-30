"""Given a list of integers that might contain duplicates, nums, return all possible subsets, otherwise known as the power set.

Time: O(2**n)
Space: O(1)
"""


def subsets:
    power_set = []
    dfs(sorted(nums), 0, [], power_set)
    return power_set


def dfs(nums, index, path, power_set):
    power_set.append(path)
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        dfs(nums, i + 1, path + [nums[i]], power_set)
