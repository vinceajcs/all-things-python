"""Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number -
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

We can solve this with a level order traversal and saving the paths of each root to leaf.

Time: O(n)
Space: O(n)
"""


def sum_root_to_leaf(root):
    if not root:
        return 0

    level, result = [(root, str(root.val))], []

    while level:
        next_level = []
        for node, path in level:
            if not node.left and not node.right:
                result.append(path)

            if node.left:
                next_level.append((node.left, path + str(node.left.val)))
            if node.right:
                next_level.append((node.right, path + str(node.right.val)))

        level = next_level

    return sum([int(x) for x in result])
