from stack import *


def reverse_file(filename):
    stack = Stack()
    file = open(filename)
    for line in file:
        stack.push(line.rstrip('\n'))
    file.close()

    output = open(filename, 'w')
    while not stack.is_empty():
        output.write(stack.pop() + '\n')
    output.close()
