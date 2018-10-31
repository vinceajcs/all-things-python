"""Given two words and a dictionary of words, find the length of shortest transformation sequence from the begin word to the end word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the dictionary.

We can model this as a shortest paths between two nodes problem.
We can use BFS to get the shortest path from the source node (begin word) to the end word node.

Time: O(L*n)
Space: O(n)
"""


def word_ladder(begin_word, end_word, word_list):

    word_list = set(word_list)
    queue = collections.deque([(begin_word, 1)])

    while queue:
        word, length = queue.popleft()

        if word == end_word:
            return length

        for i in range(len(word)):
            for c in string.ascii_lowercase:
                next_word = word[:i] + c + word[i + 1:]
                if next_word in word_list:
                    word_list.discard(next_word)
                    queue.append((next_word, length + 1))

    return 0
