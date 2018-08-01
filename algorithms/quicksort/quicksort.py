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
        elif p < S.first():
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
