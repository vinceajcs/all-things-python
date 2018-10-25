"""Sorting."""


def find_kth_largest(nums, k):
    return sorted(nums, reverse=True)[k - 1]


"""Using a min-heap."""


def find_kth_largest(nums, k):
    heap = [n for n in nums]

    heapq.heapify(heap)

    for _ in range(len(nums) - k):
        heapq.heappop(heap)

    return heapq.heappop(heap)


def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[k - 1]


"""Using quickselect."""


def find_kth_largest(nums, k):
    if not nums:
        return nums[0]

    pivot = random.choice(nums)

    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    if k <= len(greater):
        return find_kth_largest(greater, k)
    elif k <= len(greater) + len(equal):
        return pivot
    else:
        j = k - len(greater) - len(equal)
        return find_kth_largest(less, j)
