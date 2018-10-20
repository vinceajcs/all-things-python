"""Given a string s and a dictionary, words, containing a list of words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
Assume the dictionary does not contain duplicate words.

We can define dp(i) as True if s[:i] can be built using words in the dictionary.

dp(i) = True if dp(j) and dp[j:i], where j is the start of a word
        False o.w.

As such, we need to find dp(len(s)), to see if s[:len(s)] can be built using words in the dictionary.

Time: O(n**2)
Space: O(n)
"""


def word_break(s, words):
    n = len(s)
    dp = [False for _ in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for word in words:
            if dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True
    return dp[-1]
