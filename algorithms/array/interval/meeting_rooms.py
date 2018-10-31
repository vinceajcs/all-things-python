"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Time: O(nlogn)
Space: O(1)
"""


def can_attend_all(intervals):
    def is_overlap(a, b):
        return a.start < b.end and b.start < a.end

    if not intervals:
        return True

    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        if is_overlap(intervals[i - 1], intervals[i]):
            return False

    return True
