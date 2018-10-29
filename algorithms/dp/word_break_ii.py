"""Similar to word break, but this time add spaces to s and return all possible sentences that can be made with words from the dictionary."""


def word_break(s, words):
    return helper(s, words, dict())


def helper(s, words, memo):
    if not s:
        return []
    if s in memo:
        return memo[s]

    sentence = []

    for word in words:
        # s does not start with word
        if not s.startswith(word):
            continue

        # s starts with word
        if len(word) == len(s):
            sentence.append(word)
        else:
            # process rest of s
            suffixes = helper(s[len(word):], words, memo)
            for suffix in suffixes:
                suffix = word + ' ' + suffix
                sentence.append(suffix)

    memo[s] = sentence
    return sentence


"""Another way, without using recursion."""


def word_break(s, words):
    n = len(s)
    word_set = set(words)
    result = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in word_set:
                if j == 0:
                    result[i].extend(list(s[j:i]))
                else:
                    result[i].extend([e + ' ' + s[j:i] for e in result[j]])

    return result[-1]
