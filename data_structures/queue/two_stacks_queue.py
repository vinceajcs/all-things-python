class Queue:
    """Implement a queue using stacks."""

    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        self.move()
        return self.out_stack.pop()

    def first(self):
        self.move()
        return self.out_stack[-1]

    def is_empty(self):
        return (not self.in_stack) and (not self.out_stack)

    # if out-stack is empty, push all elements from in-stack to out-stack
    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
