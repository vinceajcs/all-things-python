"""Invert a binary tree.

Time: O(n)
Space: O(n)
"""


# recursive
def invert_binary_tree(root):
    if root:
        root.left, root.right = inverse_binary_tree(root.right), inverse_binary_tree(root.left)
    return root


# iterative - BFS
def invert_binary_tree(root):
    if not root:
        return root

    queue = collections.deque([root])

    while queue:
        node = queue.popleft()

        node.left, node.right = node.right, node.left

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root


# iterative - DFS
def invert_binary_tree(root):
    if not root:
        return root

    stack = [root]

    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return root
