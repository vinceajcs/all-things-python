"""Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:
push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:
Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
"""


class FreqStack:
    def __init__(self):
        self.freq = collections.Counter()  # maps element -> freq
        self.lookup = collections.defaultdict(list)  # maps freq -> elements with that freq
        self.max_freq = 0

    def push(self, x):
        freq, lookup = self.freq, self.lookup
        freq[x] += 1
        self.max_freq = max(self.max_freq, freq[x])
        lookup[freq[x]].append(x)  # lookup maps freq -> elements with that freq

    def pop(self):
        freq, lookup, max_freq = self.freq, self.lookup, self.max_freq
        x = lookup[max_freq].pop()  # get top element with highest freq

        # if there are no more elements with the max freq, decrement max freq
        if not lookup[max_freq]:
            self.max_freq -= 1

        freq[x] -= 1
        return x
