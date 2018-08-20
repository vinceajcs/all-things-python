def quick_sort(S):
    """Sorts the elements of queue S using quicksort."""
    n = len(S)
    if n < 2:
        return

    # divide
    pivot = S.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not S.is_empty():
        if S.first() < pivot:
            L.enqueue(S.dequeue())
        elif pivot < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())

    # conquer
    quick_sort(L)
    quick_sort(G)

    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


def quick_sort2(S):
    n = len(S)
    if n < 2:
        return S
    else:
        pivot = S[0]  # choose first element as pivot
        less = [i for i in S[1:] if i <= pivot]
        greater = [i for i in S[1:] if i > pivot]
        return quick_sort2(less) + [pivot] + quick_sort2(greater)


def inplace_quick_sort(S, a, b):
    if a >= b:
        return

    pivot = S[b]
    left = a
    right = b - 1

    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1

        while left <= right and pivot < S[right]:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]

    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)


def quicksort(data):
    from collections import deque
    n = len(data)
    if n < 2:
        return data

    # divide
    data = deque(data)
    pivot = data[0]
    L = deque()
    E = deque()
    G = deque()

    while data:
        if data[0] < pivot:
            L.append(data.popleft())
        elif pivot < data[0]:
            G.append(data.popleft())
        else:
            E.append(data.popleft())

    # conquer
    L = quicksort(L)
    G = quicksort(G)

    while L:
        data.append(L.popleft())
    while E:
        data.append(E.popleft())
    while G:
        data.append(G.popleft())

    return data


test = [3, 1, 5, 6, 8, 2]
print(list(quicksort(test)))
