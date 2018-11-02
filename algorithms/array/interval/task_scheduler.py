"""You are given a char array representing tasks CPU the needs to do. It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could take on a task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

We can find the task with the highest frequency (max task) and set apart each max task with an interval n.
We fill each interval with all the other tasks. If the number of these other tasks exceeds the interval space, the we don't need idle intervals.

Time: O(n)
Space: O(1)
"""


def least_intervals(tasks, n):
    lookup = collections.Counter(tasks)
    counts = lookup.values()

    max_count = max(counts)

    intervals = (max_count - 1) * (n + 1)

    for count in counts:
        if count == max_count:
            intervals += 1

    return max(len(tasks), intervals)
