"""Merge k sorted linked lists and return one sorted list.

Idea: Compare k nodes at a time and add the smallest of the k nodes to result.
Start by comparing the heads of each k lists.
We can use a min heap to store the k nodes at a time; top element in heap is the smallest.

Time: O(nklogk)
Space: O(n)
"""


def merge_k_lists(lists):
    # create min heap with first k elements (head node of each of the k lists)
    h = [(l.val, index) for index, l in enumerate(lists) if l]
    heapq.heapify(h)

    head = cur = Node(0)
    while h:
        # get min element
        min_val, min_index = heapq.heappop(h)
        # add min element to result list
        cur.next = Node(min_val)
        cur = cur.next

        # add next element from min_index list to heap
        if lists[min_index].next:
            lists[min_index] = lists[min_index].next
            heapq.heappush(h, (lists[min_index].val, min_index))

    return head.next


"""Using divide and conquer. Idea is to pair off each list among the k lists, and merge each pair.
After first iteration, k lists -> k/2 lists, then k/2 -> k/4 -> k/8...and so on.
We do this until there is only one list left.

n nodes per level, logk levels.
Time: O(nlogk)
Space: O(1)
"""


def merge_k_lists(lists):
    return helper(lists, 0, len(lists) - 1)


def helper(lists, start, end):
    if start > end:
        return None
    if start == end:
        return lists[start]

    mid = (start + end) // 2
    left = helper(lists, start, mid)
    right = helper(lists, mid + 1, end)
    return merge(left, right)


def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = merge(l1.next, l2)
        return l1
    else:
        l2.next = merge(l2.next, l1)
        return l2
