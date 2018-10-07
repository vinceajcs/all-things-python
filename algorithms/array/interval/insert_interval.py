"""Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
Assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], new_interval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Note: clarify if [1,2] and [2,3] are considered overlapping!

Time: O(n)
Space: O(1)
"""


def insert_interval(intervals, new_interval):
    merged = []

    if not intervals:
        return [new_interval] if new_interval else merged

    # insert new interval into interval list while maintaining sorted order
    i = 0
    # find the index at which to insert the new interval
    while i < len(intervals):
        if intervals[i].start > new_interval.start:
            break
        i += 1
    intervals.insert(i, new_interval)

    # iterate through all intervals and merge overlaps
    for interval in intervals:
        if not merged:
            merged.append(interval)
            continue

        if not overlap(merged[-1], interval):
            merged.append(interval)
        else:
            merged[-1] = merge_overlaps(merged[-1], interval)

    return merged


"""Helper functions."""


def overlap(a, b):
    return a.start <= b.end and b.start <= a.end


def merge_overlaps(a, b):
    return Interval(min(a.start, b.start), max(a.end, b.end))
