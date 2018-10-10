"""Given an array of numbers, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Assume k is always valid, and 1 ≤ k ≤ n for non-empty array.

Idea: Use a queue to find the max for each window.
Maintain the queue such that it is sorted in descending order (e.x. 3, 2, 1).
The first element in the queue has to be the max for a window.

1. When the window moves to the right, remove the elements smaller than the new window element (leftmost element in window).
In other words, remove elements from the end of queue until last element in the queue is greater than the new window element.
If none of the elements in the queue are greater, then the queue will become empty.

2. Add the new window element to the end of the queue.

3. Remove the first element in the queue if it is no longer in the window.

4. Add max of current window to result.

Time: O(n)
Space: O(k)
"""


def max_sliding_window(nums, k):
    result = []
    dq = collections.deque()

    for i, n in enumerate(nums):
        # remove smaller elements than n from back of deque
        while dq and nums[dq[-1]] <= n:
            dq.pop()

        # add current index/number
        dq.append(i)

        # remove first element from queue if it's no longer in the window
        if i - dq[0] == k:
            dq.popleft()

        # add max of window to result
        if i + 1 >= k:
            result.append(nums[dq[0]])

    return result
