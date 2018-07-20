def reverse_seq(S, start, stop):
    """Reverses n elements of a sequence S, using linear recursion.
    Swaps first and last elements, then recursively reverses remaining elements."""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse_seq(S, start + 1, stop - 1)

    return S


test = [4, 3, 6, 2, 8, 9, 5]
print(reverse_seq(test, 0, len(test)))  # test changes here


def reverse_seq2(S):
    copy = S[:]  # Creates copy
    return copy[::-1]  # Slicing notation


test = [4, 3, 6, 2, 8, 9, 5]
print(reverse_seq2(test))

print(test)  # test stays the same after call to reverse_seq2


def reverse_seq_iterative(S):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1

    return S


print(reverse_seq_iterative(test))
