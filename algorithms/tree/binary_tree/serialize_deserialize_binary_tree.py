"""Design an algorithm to serialize and deserialize a binary tree."""


def serialize(root):
    # serialize using preorder
    def preorder(node):
        if node:
            nodes.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        else:
            nodes.append('#')

    nodes = []
    preorder(root)
    return ' '.join(nodes)


def deserialize(data):
    # use an iterator
    def build_tree():
        node = next(nodes)

        if node == '#':
            return None

        root = Node(int(node))
        root.left = build_tree()
        root.right = build_tree()

        return root

    nodes = iter(data.split())
    return build_tree()
