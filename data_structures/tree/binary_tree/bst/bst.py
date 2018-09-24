"""Implementation of a BST with size, insert and delete methods."""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def size(self):
        return self.size_helper(self.root)

    def size_helper(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.size_helper(root.left) + self.size_helper(root.right)

    def insert(self, data):
        if self.root:
            return self.insert_helper(self.root, data)
        else:
            self.root = Node(data)
            return True

    def insert_helper(self, root, data):
        if root.data == data:
            return False
        elif data < root.data:
            if root.left:
                return self.insert_helper(root.left, data)
            else:
                root.left = Node(data)
                return True
        else:
            if root.right:
                return self.insert_helper(root.right, data)
            else:
                root.right = Node(data)
                return True

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        elif data > root.data:
            return self.search_helper(root.right, data)
        else:
            return self.search_helper(root.left, data)

    @property
    def root(self):
        return self.root
