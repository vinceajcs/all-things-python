"""Given the inorder and postorder traversals of a tree, construct the binary tree.

Time: O(n)
Space: O(n)
"""


def build_tree(inorder, postorder):
    if not inorder or not postorder:
        return None

    # find root node (last element in postorder is root)
    root = Node(postorder.pop())
    root_index = inorder.index(root.val)

    # split into two subproblems
    root.right = build_tree(inorder[root_index + 1:], postorder)
    root.left = build_tree(inorder[:root_index], postorder)

    return root
