"""Given a list of numbers and a target number, find all unique combinations in the list where the numbers sums to target.
The same repeated number may be chosen from candidates an unlimited number of times.

Example 1:
Input: candidates = [2,3,6,7], target = 7
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Time: O(n**k)
Space: O(k)
"""


def combination_sum(nums, target):
    combinations = []
    dfs(sorted(nums), target, 0, [], combinations)
    return combinations


def dfs(nums, target, index, path, combinations):
    if target < 0:
        return

    # found a combination!
    if target == 0:
        combinations.append(path)
        return

    for i in range(index, len(nums)):
        dfs(nums, target - nums[i], i, path + [nums[i]], combinations)
