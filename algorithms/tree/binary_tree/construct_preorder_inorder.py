"""Given preorder and inorder traversal of a tree, construct the binary tree.
Assume that duplicates do not exist in the tree.

Idea:
1. Find root
2. Build left subtree
3. Build right subtree

Time: O(n)
Space: O(n)
"""


def build_tree(preorder, inorder):
    if inorder:
        # first element in preorder should be the root node, and then we find root within inorder
        root_index = inorder.index(preorder.pop(0))
        root = Node(inorder[root_index])
        # split into two subproblems
        root.left = build_tree(preorder, inorder[:root_index])
        root.right = build_tree(preorder, inorder[root_index + 1:])

        return root


"""Another way using a dict."""


def build_tree(preorder, inorder):
    lookup = {}
    for i, num in enumerate(inorder):
        lookup[num] = i
    return helper(lookup, preorder, inorder, 0, 0, len(inorder))


def helper(lookup, preorder, inorder, pre_start, in_start, in_end):
    if in_start == in_end:
        return None

    root = Node(preorder[pre_start])
    # i is the index of the root in inorder
    i = lookup[preorder[pre_start]]

    root.left = helper(lookup, preorder, inorder, pre_start + 1, in_start, i)
    root.right = helper(lookup, preorder, inorder, pre_start + 1 + i - in_start, i + 1, in_end)

    return root
