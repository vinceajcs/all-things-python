"""Given an unsorted array of integers, find the length of the longest consecutive sequence.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].

Idea:
1. Turn input array into a set of nums (this takes linear time); it takes constant time to check if we have a number in the set
2. Iterate through the set once. For each number, if nums[i]-1 is not in the set, then nums[i] is the start of a streak.
3. Extend each streak for as long as possible. Record the streak when it ends, and compare with global max.

Time: O(n)
Space: O(n)
"""


def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums = set(nums)

    longest = 0

    for n in nums:
        # start new streak
        if n - 1 not in nums:
            x = n + 1
            # extend streak
            while x in nums:
                x += 1
            # streak ended; record streak
            cur_longest = x - n

            # compare with longest streak recorded
            longest = max(longest, cur_longest)

    return longest
