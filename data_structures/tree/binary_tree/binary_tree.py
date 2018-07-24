class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, val):
        if self.left == None:
            self.left = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.left = self.left
            self.left = t

    def insert_right(self, val):
        if self.right == None:
            self.right = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.right = self.right
            self.right = t

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_root(self, val):
        self.val = val

    def get_root(self):
        return self.val
