def knapsack(weights):
    """Given a list of weights, determine all sums that can be constructed using the weights."""

    n = len(weights)
    max_sum = sum(weights)

    result = []

    dp = [False for _ in range(max_sum + 1)]
    dp[0] = True

    for i in range(1, n + 1):
        # update dp from right to left for each new weight
        for x in range(max_sum, -1, -1):
            if dp[x]:
                dp[x + weights[i - 1]] = True

    for i in range(len(dp)):
        if dp[i]:
            result.append(i)

    return result  # returns all possible sums that can be constructed given a list of weights

    # return dp


test = [1, 3, 3, 5]
# all sums from 0 to 12 should be possible, except for 2 and 10
print(knapsack(test))
