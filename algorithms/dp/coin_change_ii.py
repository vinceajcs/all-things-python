"""You are given coins of different denominations and a total amount of money.
Compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.


dp(i, j) = number of combinations to make amt j using the first i types of coins

base case: dp(i, 0) = 1

dp(i, j) = dp(i-1, j) if we choose not to use the ith coin (only use first i-1 coins)
         = dp(i, j-coins[i-1]) if we use the ith coin

Time: O(len(coins) * amt)
Space: O(len(couns) * amt)
"""


def coin_change(coins, amt):
    n = len(coins)

    dp = [[0] * (amt + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, amt + 1):
            if j >= coins[i - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]  # use ith coin
            else:
                dp[i][j] = dp[i - 1][j]  # dont use ith coin

    return dp[n][amt]


"""Using less space, since dp[i][j] only relies on dp[i-1][j] and dp[i][j-coins[i]]."""


def coin_change(coins, amt):
    dp = [0] * (amt + 1)
    dp[0] = 1
    for i in coins:
        for j in range(1, amt + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[amt]
