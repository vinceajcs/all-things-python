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
