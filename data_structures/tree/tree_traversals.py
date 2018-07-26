from collections import deque


def preorder(tree):
    if tree:
        print(tree.get_root())
        preorder(tree.get_left())
        preorder(tree.get_right())


def inorder(tree):
    if tree:
        inorder(tree.get_left())
        print(tree.get_root())
        inorder(tree.get_right())


def postorder(tree):
    if tree:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree.get_root())


def bft(tree):
    queue = deque([tree.get_root()])
    while queue is not None:
        node = queue.popleft()
        print(node)

        if node.get_left() is not None:
            queue.append(node.get_left())

        if node.get_right() is not None:
            queue.append(node.get_right())
