def disjoint_naive(A, B, C):
    """Return True if no element is common to all three sets.
    Worst-case O(n**3).
    """
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False  # common value exists
    return True  # sets are disjoint


def disjoint_quadratic(A, B, C):
    for a in A:
        for b in B:
            if a == b:  # check for value in set C only if value is found in both A and B
                for c in C:
                    if a == c:
                        return False
    return True
