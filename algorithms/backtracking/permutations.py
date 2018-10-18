"""Given a list of distinct nums, generate all permutations."""


# recursive
def permutations(nums):
    result = []
    backtrack(nums, [], result)
    return result


def backtrack(nums, path, result):
    if not nums:
        result.append(path)

    for i in range(len(nums)):
        backtrack(nums[:i] + nums[i + 1:], path + [nums[i]], result)


# iterative
def permutations(nums):
    permutations = [[]]
    for n in nums:
        new_permutations = []
        for p in permutations:
            for i in range(len(p) + 1):
                new_permutations.append(p[:i] + [n] + p[i:])  # insert n
        permutations = new_permutations
    return permutations
