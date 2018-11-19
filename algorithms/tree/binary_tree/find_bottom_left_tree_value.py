"""Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1

Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

We can use a level order traversal and get the first (leftmost) value in the last level.

Time: O(n)
Space: O(h)
"""


def find_bottom_left(root):
    if root is None:
        return []

    level, result = [root], []

    while level:
        current, next_level = [], []
        for node in level:
            current.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        result.append(current)

    return result[-1][0]
