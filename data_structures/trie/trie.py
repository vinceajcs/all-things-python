"""Implementation of a trie, otherwise known as a prefix tree.
Insert, search and starts_with methods all are O(n), where n is the length of a word.
"""


from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True

    def search(self, word):
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return False
        return True
