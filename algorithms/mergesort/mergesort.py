def merge_sort(S):
    """Sorts the input list using the merge sort algorithm."""
    if len(S) <= 1:
        return S
    mid = len(S) // 2
    S1 = merge_sort(S[:mid])
    S2 = merge_sort(S[mid:])
    return merge(S1, S2)


def merge(S1, S2):
    """Merges two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while True:
        if i >= len(S1):          # If S1 list is finished,
            result.extend(S2[j:])  # add remaining items from S2
            return result

        if j >= len(S2):          # If S2 list is finished
            result.extend(S1[i:])
            return result

        # Both lists still have items, copy smaller item to result.
        if S1[i] <= S2[j]:
            result.append(S1[i])
            i += 1
        else:
            result.append(S2[j])
            j += 1


def merge_recursive(S1, S2):
    if not S1:
        return S2
    if not S2:
        return S1
    if S1[0] < S2[0]:
        return [S1[0]] + merge(S1[1:], S2)
    return [S2[0]] + merge(S1, S2[1:])
