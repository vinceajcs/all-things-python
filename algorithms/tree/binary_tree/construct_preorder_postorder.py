"""Create any binary tree using the given preorder and postorder traversals.

Time: O(n)
Space: O(n)
"""


def build_tree(preorder, postorder):
    stack = [Node(preorder[0])]
    j = 0
    for v in preorder[1:]:
        node = Node(v)
        # if pre and post have the same value that means we just finished constructing a subtree
        # or, we have visted all the children of that node (stack[-1].val)
        while stack[-1].val == post[j]:
            stack.pop()
            j += 1

        if not stack[-1].left:
            stack[-1].left = node
        else:
            stack[-1].right = node

        stack.append(node)

    return stack[0]


def build_tree(preorder, postorder):
    """
    The first element in "pre" and the last element in "post" should both be the value of the root.
    The second to last of "post" should be the value of right child of the root.
    So we can find the index to split "left" and "right" children in "pre".
    """

    if not pre or not post:
        return None

    root = Node(pre[0])

    if len(pre) == 1:
        return root

    right_index = preorder.index(postorder[-2])
    root.left = build_tree(preorder[1: right_index], postorder[:right_index - 1])
    root.right = build_tree(preorder[right_index:], postorder[right_index - 1: -1])

    return root
