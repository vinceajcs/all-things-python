"""Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Idea: Use Kadane's algorithm, which is used to find the max contiguous subarray.
Instead of using the array of stock prices, we can use an array of differences prices[i] - prices[i-1].

For example, we would turn [7, 1, 5, 3, 6, 4] into [0, -6, 4, -2, 3, -2].

We can keep track of the sum as we pass through the array, and if the sum falls below 0, we reset it to 0.

Time: O(n)
Space: O(1)
"""


def max_profit(prices):
    if not prices:
        return 0

    cur_sum, max_sum = 0, 0
    for i in range(1, len(prices)):
        difference = prices[i] - prices[i - 1]
        cur_sum = max(0, cur_sum + difference)
        max_sum = max(max_sum, cur_sum)

    return max_sum
