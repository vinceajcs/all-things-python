def inverse_binary_tree(root):
    if root is not None:
        root.left, root.right = inverse_binary_tree(root.right), inverse_binary_tree(root.left)
    return root


def inverse_binary_tree(root):
    from collections import deque
    if root:
        nodes = deque([])
        nodes.append(root)

        while nodes:
            node = nodes.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
    return root
