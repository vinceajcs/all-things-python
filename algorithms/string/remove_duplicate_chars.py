"""Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once.
Make sure your result is the smallest in lexicographical order among all possible results.

Initially we can get the frequency of each char in the string, using a Counter.
Then, we iterate through the string. For each char, check if there is a smaller char (lexicographical order wise) in front of it.
If there is a smaller char, check if there is another instance of the current char.
If there is, remove that char from the result and add the smaller char.
After iterating through the entire string, our result contains all unique chars in lexicographical order.

Time: O(n)
Space: O(1)
"""


def remove_duplicates(s):
    counter, visited, stack = collections.Counter(s), set(), []

    for c in s:
        counter[c] -= 1

        if c in visited:
            continue

        while stack and stack[-1] > c and counter[stack[-1]] > 0:
            visited.remove(stack.pop())

        stack.append(c)
        visited.add(c)

    return ''.join(stack)
