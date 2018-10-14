"""Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Time: O(n)
Space: O(n)
"""


# recursive
def is_balanced(root):

    def check(root):
        if root is None:
            return 0
        left = check(root.left)
        right = check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


# iterative, based on postorder traversal
def is_balanced(root):
    stack, node = [], root
    last, depths = None, collections.defaultdict(int)
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right = depths[node.left], depths[node.right]
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                last, node = node, None
            else:
                node = node.right
    return True
