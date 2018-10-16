"""Given a binary search tree and a node in it, find the inorder successor of that node in the BST.

Idea: Traverse the BST inorder.
Since there are no duplicates in a BST, to find the successor, find the smallest element that is greater than the input node.

Time: O(n)
Space: O(1)
"""


def inorder_successor(root, p):
    successor = None
    while root:
        if p.val < root.val:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor
