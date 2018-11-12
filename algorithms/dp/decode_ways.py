"""A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

We can define dp(i) as the number of ways to decode a substring of a string s up to index i.

We look at two chars at a time - those at index i and i-1 - because 26 is the max number that can be encoded to.

There are 4 possibilities:
1. prev and curr are both 0 -> return 0
2. prev value is 0 -> use only current value
3. curr value is 0 -> only use prev value
4. both prev and curr are not 0; we can use both values to get dp(i+1)

Time: O(n)
Space: O(n)
"""


def num_decodings(s):
    if not s or s[0] == '0':
        return 0

    n = len(s)

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(1, n):
        prev = s[i - 1]
        curr = s[i]

        if (prev == '0' and curr == '0') or (curr == '0' and prev + curr > '26'):
            return 0
        elif prev == '0' or prev + curr > '26':
            dp[i + 1] = dp[i]
        elif curr == '0':
            dp[i + 1] = dp[i - 1]
        else:
            dp[i + 1] = dp[i] + dp[i - 1]

    return dp[n]
