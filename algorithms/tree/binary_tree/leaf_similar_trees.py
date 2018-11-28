"""Given two binary trees, determine if they are leaf similar.
Two binary trees are considered to be leaf similar if they have the same leaf sequence.

We can use an inorder traversal on both trees to find their respective leaf sequences.

Time: O(n+m)
Space: O(n+m)
"""


def leaf_similar(root1, root2):
    return get_leafs(root1) == get_leafs(root2)


def get_leafs(root):
    result = []
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if not root.left and not root.right:
            result.append(root.val)
        root = root.right

    return result
