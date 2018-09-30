def compose_string(words):
    """This is an inefficient way to produce a new string of only alphabetic characters a given string.
    Strings are immutable and thus the line letters += c creates a new string instance every time."""
    letters = ''
    for c in words:
        if c.isalpha():
            letters += c
    return letters


def compose_string_linear(words):
    """This is a better way to guarantee linear time composition of a string, using a temp list."""
    temp = []
    for c in words:
        if c.isalpha():
            temp.append(c)
    letters = ''.join(temp)
    return letters


def compose_string_linear(words):
    """This is the same as the function above, except it uses list comprehension syntax instead."""
    return ''.join([c for c in words if c.isalpha()])
