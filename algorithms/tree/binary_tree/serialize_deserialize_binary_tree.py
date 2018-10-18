"""Design an algorithm to serialize and deserialize a binary tree."""


def serialize(root):

    def build_string(node):
        if node:
            nodes.append(str(node.val))
            build_string(node.left)
            build_string(node.right)
        else:
            nodes.append('#')

    nodes = []
    nodes = build_string(root)
    return ' '.join(nodes)


def deserialize(root):

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
