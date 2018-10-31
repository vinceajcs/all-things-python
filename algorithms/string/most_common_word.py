"""Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive.
The answer is in lowercase.

Time: O(n)
Space: O(n)
"""


def most_common_word(paragraph, banned):
    if not paragraph:
        return ''

    words = re.findall(r'\w+', paragraph.lower())  # strip punctuation
    not_banned = [w for w in words if w not in banned]  # get all non banned words in paragraph
    counter = collections.Counter(not_banned)
    return counter.most_common()[0][0]
