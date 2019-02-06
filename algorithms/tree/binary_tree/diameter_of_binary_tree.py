"""Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree:
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

Time: O(n)
Space: O(1)
"""


def diameter(root):
    self.longest_path = 0  # global max

    def depth(node):
        if not node:
            return 0
        left, right = depth(node.left), depth(node.right)
        self.longest_path = max(self.longest_path, left + right)
        return 1 + max(left, right)

    depth(root)
    return self.longest_path
