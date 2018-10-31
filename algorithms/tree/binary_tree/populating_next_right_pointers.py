"""Given a perfect binary tree, populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

We can traverse the binary tree level by level.

Time: O(n)
Space: O(n)
"""


def connect(root):
    if not root:
        return

    queue = collections.deque()
    queue.append(root)
    queue.append(None)

    while queue:
        node = queue.popleft()

        if node:
            node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            if len(queue) > 0:
                queue.append(None)


"""Another way, recursively."""


def connect(root):
    if not root:
        return

    if root.left:
        root.left.next = root.right
    if root.right and root.next:
        root.right.next = root.next.left

    connect(root.left)
    connect(root.right)


"""Another iterative solution."""


def connect(root):
    while root and root.left:
        next_node = root.left

        while root:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None

            root = root.next

        root = next_node
