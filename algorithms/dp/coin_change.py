"""Given coins of different denominations and a total amount of money amount, compute the fewest number of coins needed to make up that amount.

Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1


Here, we can think of cc(i) = min number of coins needed to make amount i using coins.
In this example,

cc(i) = 0 if i = 0
        min(cc(i-1)+1, cc(i-2)+1, cc(i-5)+1) o.w.

Let's say we choose coin 5 first. Then, our remaining task is to form (11-5=6) using the remaining coins.

Time: O(amount*n)
Space: O(amout)
"""


def coin_change(coins, amount):
    MAX = float('inf')
    cc = [MAX for _ in range(amount + 1)]
    cc[0] = 0

    for i in range(1, amount + 1):
        cc[i] = min([cc[i - coin] if i - coin >= 0 else MAX for coin in coins]) + 1

    return cc[-1] if cc[-1] != MAX else -1
