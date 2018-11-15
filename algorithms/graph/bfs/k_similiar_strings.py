"""Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.
Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:
Input: A = "ab", B = "ba"
Output: 1

Example 2:
Input: A = "abc", B = "bca"
Output: 2

Example 3:
Input: A = "abac", B = "baca"
Output: 2

Example 4:
Input: A = "aabc", B = "abca"
Output: 2
"""


def k_similar(A, B):
    if A == B:
        return 0

    queue, visited = collections.deque(), set()

    k = 0

    queue.append((A, 0))
    visited.add(A)

    def get_neighbors(s):
        i = 0
        while s[i] == B[i]:
            i += 1

        node = list(s)
        for j in range(i + 1, len(s)):
            if s[j] == B[i]:
                node[i], node[j] = node[j], node[i]
                yield ''.join(node)
                node[j], node[i] = node[i], node[j]

    while queue:

        s, level = queue.popleft()

        if s == B:
            k = level
            break

        for neighbor in get_neighbors(s):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return k
