"""On a staircase, the ith step has some non-negative cost cost[i] assigned.
Once you pay the cost, you can either climb one or two steps.
Find minimum cost to reach the top of the floor - you can either start from the step with index 0, or the step with index 1.

Time: O(n)
Space: O(n)
"""


def min_cost(costs):
    dp = [0] * len(costs)

    dp[0], dp[1] = cost[0], cost[1]

    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 2] + cost[i],
                    dp[i - 1] + cost[i])

    return min(dp[-2], dp[-1])


"""Using less space."""


def min_cost(costs):
    pre, cur = cost[0], cost[1]
    for i in range(2, len(cost)):
        pre, cur = cur, min(pre + cur) + cost[i]

    return min(pre, cur)
