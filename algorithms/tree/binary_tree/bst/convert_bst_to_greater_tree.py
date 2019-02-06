"""Given a BST, convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key.

Example:
Input:
          5
        /   \
       2     13

Output:
         18
        /   \
      20     13

Idea: We can traverse the BST in reverse inorder.

Time: O(n)
Space: O(1)
"""


def convert_bst(root):
    self.val = 0  # 'global' variable to keep track of suffix sum

    def visit(root):
        if root:
            visit(root.right)
            root.val += self.val
            self.val = root.val
            visit(root.left)

    visit(root)
    return root
