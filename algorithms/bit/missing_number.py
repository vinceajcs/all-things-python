"""Given a list containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the list."""


"""Using Gauss' formula."""


def missing_number(nums):
    n = len(nums)
    return (n * (n + 1) // 2) - sum(nums)


"""Using XOR."""


def missing_number(nums):
    n = len(nums)
    for i, num in enumerate(nums):
        n ^= i ^ num
    return n
