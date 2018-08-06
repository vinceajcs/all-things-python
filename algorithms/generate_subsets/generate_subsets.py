def generate_subsets(S):
    r = [[]]
    for e in S:
        r += [x + [e] for x in r]
    return r


s = [0, 1, 2]
print(generate_subsets(s))
