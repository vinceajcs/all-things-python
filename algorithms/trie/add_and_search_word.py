"""Design a data structure that supports the following two operations:

addWord(word)
search(word)

Note: search(word) can search a literal word or a regular expression string containing only letters a-z or '.'.
A '.' means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True

    def search(self, word):
        node = self.root
        self.found = false
        self.dfs(node, word)
        return self.found

    def dfs(self, node, word):
        if not word:
            if node.is_word:
                self.found = True
                return
        elif word[0] == '.':
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            # must be a letter, assuming words only consist of lowercase letters a-z
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])
