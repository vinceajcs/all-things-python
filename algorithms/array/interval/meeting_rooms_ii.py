"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1

Idea: We can use a min heap to store end times of each interval.
The room at the top of the min heap is then the one that will be free at the earliest time.
If the room at the top is not free, no other room is. In this case, we allocate a new room.

Time: O(nlogn)
Space: O(n)
"""


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x.start)

    heap = []  # stores the end time of intervals

    for i in intervals:
        if heap and i.start >= heap[0]:
            # means two intervals can use the same room
            heapq.heapreplace(heap, i.end)  # pop then push
        else:
            # a new room is allocated
            heapq.heappush(heap, i.end)

    return len(heap)
