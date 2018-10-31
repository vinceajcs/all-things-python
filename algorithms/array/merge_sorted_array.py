"""Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.

Example:

Input:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Time: O(m+n)
Space: O(1)
"""


def merge(A, B, m, n):
    while m > 0 and n > 0:
        if A[m - 1] >= B[n - 1]:
            A[m + n - 1] = A[m - 1]
            m -= 1
        else:
            A[m + n - 1] = B[n - 1]
            n -= 1

    if n > 0:
        A[:n] = B[:n]
