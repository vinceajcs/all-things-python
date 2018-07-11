class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return(str(self.data))


left = Tree(2)
right = Tree(3)

tree = Tree(1, left, right)
tree = Tree(1, Tree(2), Tree(3))


def total(tree):
    if tree is None:
        return 0
    return total(tree.left) + total(tree.right) + tree.data


print(total(tree))
