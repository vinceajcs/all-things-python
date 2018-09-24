class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, val):
        self.data = val

    @property
    def left(self):
        return self.left

    @property
    def right(self):
        return self.right


class BinaryTree:
    def __init__(self, root):
        self.root = None

    def insert_left(self, item):
        new = TreeNode(item)
        node = self.root

        if node is None:
            self.root = new
        else:
            while node.left:
                node = node.left
            node.left = new

    def insert_right(self, item):
        new = TreeNode(item)
        node = self.root

        if node is None:
            self.root = new
        else:
            while node.right:
                node = node.right
            node.right = new
