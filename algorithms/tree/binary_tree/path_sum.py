"""Given a binary tree and a sum, determine if the leaf has a roof-to-leaf path s.t. adding up all the values along the path equals the given sum.

Time: O(n)
Space: O(n)
"""


"""Using BFS and recording the paths."""


def has_path_sum(root, path_sum):
    if not root:
        return False

    queue = collections.deque([(root, [root.val])])

    while queue:
        node, path = queue.popleft()

        if node.left is None and node.right is None:  # found a leaf
            if sum(path) == path_sum:
                return True

        if node.left:
            queue.append((node.left, path + [node.left.val]))

        if node.right:
            queue.append((node.right, path + [node.right.val]))

    return False


"""Another idea using recursion."""


def has_path_sum(root, path_sum):
    if not root:
        return False

    if root.left is None and root.right is None and root.val == path_sum:
        return True

    path_sum -= root.val

    return has_path_sum(root.left, path_sum) or has_path_sum(root.right, path_sum)
