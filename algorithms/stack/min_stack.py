"""Using tuples to store the data + current minimum."""


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        current_min = self.get_min()
        if current_min == None or x < current_min:
            current_min = x
        self.stack.append((x, current_min))

    def pop(self):
        self.stack.pop()

    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]

    def get_min(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]


"""Using two stacks: one for data, other for minimums."""


class MinStack:
    def __init__(self):
        self.stack, self.min_stack = [], []

    def push(self, x):
        self.stack.append(x)

        current_min = self.min_stack[-1]
        if not min_stack or x < current_min:
            self.min_stack.append(x)
        else:
            self.min_stack.append(current_min)

    def pop(self):
        # pop both stacks!
        self.stack.pop()
        self.min_stack.pop()

    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            return None
        else:
            return self.min_stack[-1]
