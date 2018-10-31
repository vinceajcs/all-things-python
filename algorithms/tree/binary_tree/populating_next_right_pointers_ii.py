"""Same problem, but this time the binary tree is not perfect."""


def connect(self, root):
    if not root:
        return

    level, next_level = [root], []   # queue records the previous level

    while level:
        node = level.pop(0)
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
        if level:
            node.next = level[0]

        if not level and next_level:
            level, next_level = next_level, level


"""Using constant space."""


def connect(root):
    node = dummy = Node(0)

    while root:
        node.next = root.left
        if node.next:
            node = node.next

        node.next = root.right
        if node.next:
            node = node.next

        root = root.next
        if not root:
            node, root = dummy, dummy.next
