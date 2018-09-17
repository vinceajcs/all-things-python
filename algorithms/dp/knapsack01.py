def naive(weights, values, capacity, n):
    """Given a list of weights and values of n items to be placed in a knapsack,
    determine the max value of items in the knapsack given its capacity.
    """
    if n == 0 or capacity == 0:
        return 0

    # weight of nth item is > capacity, thus item cannot be included
    if weights[n - 1] > capacity:
        return naive(weights, values, capacity, n - 1)

    else:
        # case 1: include current item in the knapsack, then find max value given capacity - weight of current item
        include = values[n - 1] + naive(weights, values, capacity - weights[n - 1], n - 1)
        # case 2: exlcude current item from the knapsack, find max value given remaining items
        exclude = naive(weights, values, capacity, n - 1)

        # find max of two cases
        return max(include, exclude)


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(weights)
# max value should be 220 (items with values of 100 and 120, weights 20 and 30, respectively)
print(naive(weights, values, capacity, n))


# DP solution
def knapsack(weights, values, W):
    """Given a list of weights and values of n items to be placed in a knapsack,
    determine the max value of items in the knapsack given its capacity W.
    """
    n = len(weights)

    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # bottom up
    for i in range(n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[-1][-1]


print(knapsack(weights, values, capacity))
