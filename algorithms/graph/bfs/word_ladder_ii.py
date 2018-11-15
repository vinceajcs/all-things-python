"""Same as word ladder, but this time return all paths."""


def word_ladder(begin_word, end_word, word_list):
    word_list = set(word_list)
    paths = []

    level = {}
    level[begin_word] = [[begin_word]]

    while level:
        next_level = collections.defaultdict(list)

        for word in level:
            if word == end_word:
                for path in level[word]:
                    paths.append(path)
            else:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word in word_list:
                            for path in level[word]:
                                next_level[next_word].append(path + [next_word])

        word_list -= set(next_level.keys())
        level = next_level

    return paths
