"""Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Time: O(m*n)
Space: O(h)
"""


# recursive
def is_subtree(s, t):
    if not s:
        return False

    if is_same(s, t):
        return True

    return is_subtree(s.left, t) or is_subtree(s.right, t)


# iterative - BFS
def is_subtree(s, t):
    if not s:
        return False

    queue = collections.deque([s])

    while queue:
        node = queue.popleft()

        if is_same(node, t):
            return True

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


def is_same(s, t):
    if not s and not t:
        return True

    if s and t:
        return s.val == t.val and is_same(s.left, t.left) and is_same(s.right, t.right)

    return False
