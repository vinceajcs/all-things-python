def is_matched_html(raw):
    """Return True if all HTML tags are properly matched; False otherwise."""

    stack = []
    # find first '<' character
    j = raw.find('<')

    while j != - 1:
        # find next '>' character
        k = raw.find('>', j + 1)
        if k == -1:
            return False              # invalid tag

        tag = raw[j + 1:k]            # strip away < >

        if not tag.startswith('/'):   # this is opening tag
            stack.push(tag)
        else:                         # this is closing tag
            if not stack:
                return False          # nothing to match with
            if tag[1:] != stack.pop():
                return False          # mismatched delimiter

        j = raw.find('<', k + 1)      # find next '<' character

    return False if stack else True
