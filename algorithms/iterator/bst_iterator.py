"""Implement an iterator over a BST. Calling next() will return the next smallest number in the BST.

We can base the next method on an iterative inorder traversal.
"""


class BSTIterator:
    def __init__(self, root):
        self.current = root
        self.stack = []

    def has_next(self):
        return self.current is not None or self.stack

    def next(self):
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        next_node = self.stack.pop()
        self.current = next_node.right
        return next_node.val
