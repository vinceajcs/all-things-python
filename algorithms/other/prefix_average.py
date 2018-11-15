def prefix_average1(nums):
    """Returns a list s.t. for all i, result[i] equals the avg of nums[0],...,nums[i].
    This running time is O(n^2), and thus this is a quadratic-time algorithm.
    """
    n = len(nums)
    result = [0] * n

    for i in range(n):
        sum = 0
        for j in range(i + 1):
            sum += nums[j]
        result[i] = sum / (i + 1)

    return result


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avgs = prefix_average1(nums)
print(avgs)


def prefix_average2(nums):
    """Running time is still O(n^2)."""
    n = len(nums)
    result = [0] * n

    for i in range(n):
        result[i] = sum(nums[0:i + 1]) / (i + 1)

    return result


avgs = prefix_average2(nums)
print(avgs)


def prefix_average_linear(nums):
    """Running time is O(n)."""
    n = len(nums)
    result = [0] * n
    sum = 0

    for i in range(n):
        sum += nums[i]
        result[i] = sum / (i + 1)

    return result


avgs = prefix_average_linear(nums)
print(avgs)
