"""Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Idea: Use a dict to store prefix/subarray sum of the array up to a given index.

For example, if nums = [1, 3, 4, 13],

{0:1} -> sum of 0 = empty array
{0:1, 1:1} -> sum up to and including index 0 element is 1 ([1])
{0:1, 1:1, 4:1} -> ...including index 1 element is 4 ([1, 3])
{0:1, 1:1, 4:1, 8:1} -> ...including index 2 element is 8 ([1, 3, 4])
...

For each iteration we can check if there is a prefix/subarray array we can discard to obtain our desired target of k.
For example if k = 7, when we arrive at index 2, our sum will be 8 but we can see that there is a prefix sum of 1 in the array according to our dict.
Thus we can deduce that there is a contiguous subarray of sum 7 and this can be achieved by getting rid of the prefix array of sum of 1 in our current window.

Time: O(n)
Space: O(n)
"""


def subarray_sum(nums):
    lookup = collections.defaultdict(int)  # prefix sum -> num of occurences
    lookup[0] = 1  # empty array has a sum of 0
    result = 0
    current_sum = 0

    for n in nums:
        current_sum += n

        target = current_sum - k

        if target in lookup:  # found a contiguous subarray whose sum equals to k
            result += lookup[target]

        lookup[current_sum] += 1  # record occurence of current_sum

    return result
