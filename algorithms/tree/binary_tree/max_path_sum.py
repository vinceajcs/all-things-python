"""Given a non-empty binary tree, find the maximum path sum.
A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Time: O(n)
Space: O(h), where h is the height of the binary tree
"""


class Solution:
    global_max = float('-inf')

    def max_path_sum(self, root):
        self.find_max(root)
        return self.global_max

    def find_max(self, root):
        if not root:
            return 0

        # search for max path in each subtree
        left = self.find_max(root.left)
        right = self.find_max(root.right)

        left = 0 if left < 0 else left
        right = 0 if right < 0 else right

        # update global max
        self.global_max = max(self.global_max, left + right + root.val)

        # each parent node should return its own value + its max child
        return root.val + max(left, right)
