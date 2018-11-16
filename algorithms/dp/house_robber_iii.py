"""The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the root.
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.

Time: O(n)
Space: O(n)
"""


"""Naive solution."""


def rob(root):
    if not root:
        return 0

    result = 0

    # calculate money earned from robbing the grandchildren
    if root.left:
        result += self.rob(root.left.left) + self.rob(root.left.right)

    if root.right:
        result += self.rob(root.right.left) + self.rob(root.right.right)

    # either we rob the grandchildren and the current node or the children of the current node
    return max(result + root.val, self.rob(root.left) + self.rob(root.right))


"""Better solution using a dict to store solutions to overlapping subproblems."""


def rob(root):
    return helper(root, dict())


def helper(root, lookup):
    if not root:
        return 0

    if root in lookup:
        return lookup[root]

    result = 0

    if root.left:
        result += helper(root.left.left, lookup) + helper(root.left.right, lookup)

    if root.right:
        result += helper(root.right.left, lookup) + helper(root.right.right, lookup)

    result = max(result + root.val, helper(root.left, lookup) + helper(root.right, lookup))

    lookup[root] = result

    return result


"""Using a Greedy algorithm."""


def rob(root):
    result = helper(root)
    # result[0] = max money if root is not robbed, whereas result[1] = max money if root is robbed
    return max(result[0], result[1])


def helper(root):
    result = [0, 0]

    if not root:
        return result

    left = helper(root.left)
    right = helper(root.right)

    result[0] = max(left[0], left[1]) + max(right[0], right[1])
    result[1] = root.val + left[0] + right[0]

    return result
