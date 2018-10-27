"""Find the median of the two sorted arrays.

Time: O(log(m+n))
Space: O(1)
"""


def find_median(A, B):
    l = len(A) + len(B)

    if l % 2 == 1:  # odd length
        return find_kth(A, B, l // 2)
    else:  # even length
        return (find_kth(A, B, l // 2) + find_kth(A, B, l // 2 - 1)) / 2


def find_kth(A, B, k):
    if len(A) > len(B):  # ensure B has more elements
        A, B = B, A

    if not A:  # if A is empty, kth element is in B
        return B[k]

    # if k is equal to the combined length of A and B, return the max of the last element in each array
    if k == len(A) + len(B) - 1:
        return max(A[-1], B[-1])

    i = min(len(A) - 1, k // 2)
    j = min(len(B) - 1, k - i)

    if A[i] > B[j]:
        return find_kth(A[:i], B[j:], i)
    else:
        return find_kth(A[i:], B[:j], j)
