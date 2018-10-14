"""Invert a binary tree.

Time: O(n)
Space: O(n)
"""


# recursive
def invert_binary_tree(root):
    if root is not None:
        root.left, root.right = inverse_binary_tree(root.right), inverse_binary_tree(root.left)
    return root


# iterative
def invert_binary_tree(root):
    if root:
        nodes = collections.deque([])
        nodes.append(root)

        while nodes:
            node = nodes.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
    return root
