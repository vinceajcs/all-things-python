"""Given a collection of intervals, merge all overlapping intervals.

Note: clarify if [1,2] and [2,3] are considered overlapping!

Time: O(nlogn)
Space: O(1)
"""


def merge(intervals):
    merged = []
    if not intervals:
        return merged

    # sort intervals by start time
    intervals.sort(key=lambda x: x.start)

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
