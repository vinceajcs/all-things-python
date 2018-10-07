"""Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Assume the interval's end point is always bigger than its start point.
Assume [1,2] and [2,3] are NOT considered to be overlapping.

Example 1:
Input: [[1,2], [2,3], [3,4], [1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2], [1,2], [1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2], [2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Idea: find max number of intervals that are non-overlapping.
The best first interval to keep is the one that ends first, as this interval leaves more room for the rest.

1. Sort intervals by end time, ascending, then traverse intervals to get max number of non-overlapping intervals.
2. Minimum number of intervals to remove = total intervals - max number of non-overlapping intervals.


Time: O(nlogn)
Space: O(1)
"""


def overlaps_to_remove(intervals):
    intervals.sort(key=lambda x: x.end)
    end = float('-inf')

    # count keeps track of the number of non-overlapping intervals
    count = 0

    # iterate through intervals to find number of non-overlapping intervals
    for interval in intervals:
        # non-overlapping
        if interval.start >= end:
            end = interval.end
            count += 1

    # min number to remove = total intervals - # of non-overlapping intervals
    return len(intervals) - count
