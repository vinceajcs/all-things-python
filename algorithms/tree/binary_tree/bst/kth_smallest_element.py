"""Find the kth smallest element in a given BST.

We can use an inorder traversal to solve this.

Time: O(max(n, k))
Space: O(n)
"""


def kth_smallest(root, k):
    stack = []

    while root:
        while root or stack:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            break
        root = root.right

    return root.val
