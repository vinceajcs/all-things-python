def reverse_file(filename):
    stack = []
    file = open(filename)
    for line in file:
        stack.push(line.rstrip('\n'))
    file.close()

    output = open(filename, 'w')
    while stack:
        output.write(stack.pop() + '\n')
    output.close()
