"""Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Time: O(m*n)
Space: O(h)
"""


# recursive
def is_subtree(s, t):
    if is_same(s, t):
        return True
    if not s:
        return False
    return is_subtree(s.left, t) or is_subtree(s.right, t)


# iterative
def is_subtree(s, t):
    is_subtree = False

    queue = collections.deque([])
    queue.append(s)

    while queue:
        node = queue.popleft()
        if node.val == t.val:
            is_subtree = is_same(node, t)
            break
        else:
            queue.append(node.left)
            queue.append(node.right)

    return is_subtree


def is_same(s, t):
    if not s and not t:
        return True

    if s and t:
        return s.val == t.val and is_same(s.left, t.left) and is_same(s.right, t.right)

    return False
