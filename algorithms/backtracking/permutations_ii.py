"""Given a list of nums that might contain duplicates, return all possible permutations."""


# iterative
def permutations(nums):
    """Idea: avoid inserting a number after any of its duplicates."""
    permutations = [[]]
    for n in nums:
        new_permutations = []
        for p in permutations:
            for i in range(len(p) + 1):
                new_permutations.append(p[:i] + [n] + p[i:])  # insert n
                if i < len(p) and p[i] == n:  # deal with duplicates
                    break
        permutations = new_permutations
    return permutations
