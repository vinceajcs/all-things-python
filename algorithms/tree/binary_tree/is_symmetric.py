"""Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

Time: O(n)
Space: O(h)
"""


# recursive solution
def is_symmetric(root):
    if not root:
        return True

    return helper(root.left, root.right)


def helper(left, right):
    if not left and not right:
        return True

    if not left or not right or left.val != right.val:
        return False

    return helper(left.left, right.right) and helper(left.right, right.left)


# iterative solution
def is_symmetric(root):
    if not root:
        return True

    stack = []
    stack.append(root.left)
    stack.append(root.right)

    while stack:
        left, right = stack.pop(), stack.pop()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False

        stack.append(left.left)
        stack.append(right.right)

        stack.append(left.right)
        stack.append(right.left)

    return True
