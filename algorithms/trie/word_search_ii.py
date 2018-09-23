"""Given a 2d matrix board and a list of words from a dictionary, find all the words in the board.
Each word can only be made with letters in adjacent cells.

Example:

input:
words = ['oath', 'pea', 'eat', 'rain']
board = [['o', 'a', 'a', 'n'],
         ['e', 't', 'a', 'e'],
         ['i', 'h', 'k', 'r'],
         ['i', 'f', 'l', 'v']]

output: ['oath', 'eat']

Time: O(m*n*l)
Space: O(l)
"""


import unittest


def find_words(board, words):
    trie = {}
    # build trie
    for word in words:
        t = trie
        for letter in word:
            if letter not in t:
                t[letter] = {}
            t = t[letter]
        t['#'] = '#'  # mark end of word

    result = []
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            find(board, trie, '', result, i, j, m, n)
    return list(set(result))


def find(board, trie, path, result, i, j, m, n):
    # found a word
    if '#' in trie:
        result.append(path)

    if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in trie:
        return

    temp, board[i][j] = board[i][j], '@'  # mark letter so it cannot be reused

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        x, y = i + direction[0], j + direction[1]
        find(board, trie[temp], path + temp, result, x, y, m, n)

    board[i][j] = temp  # restore board


words = ['oath', 'pea', 'eat', 'rain']
board = [['o', 'a', 'a', 'n'],
         ['e', 't', 'a', 'e'],
         ['i', 'h', 'k', 'r'],
         ['i', 'f', 'l', 'v']]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_words(board, words), ['oath', 'eat'])


if __name__ == '__main__':
    unittest.main()
