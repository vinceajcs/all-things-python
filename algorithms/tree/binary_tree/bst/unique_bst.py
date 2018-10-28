"""Given n, find number of unique BSTs that store values 1...n.

Time: O(n**2)
Space: O(n)
"""


def unique_bst(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        for j in range(i + 1):
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[-1]
