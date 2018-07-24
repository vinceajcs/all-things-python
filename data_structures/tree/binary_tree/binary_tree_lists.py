"""Binary tree implementation using lists of lists."""


def binary_tree(root):
    return [root, [], []]


def insert_left(root, new_tree):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_tree, t, []])
    else:
        root.insert(1, [new_tree, [], []])
    return root


def insert_right(root, new_tree):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_tree, [], t])
    else:
        root.insert(2, [new_tree, [], []])
    return root


def get_root(root):
    return root[0]


def set_root(root, val):
    root[0] = val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]
