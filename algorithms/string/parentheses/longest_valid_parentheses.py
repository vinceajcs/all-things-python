"""Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Algorithm:
1. Scan the string from beginning to end.
2. If current character is '(', push its index to the stack.
If current character is ')' and the character at the index of the top of stack is '(',
we just found a matching pair! As a result - pop from the stack.
Otherwise, we push the index of ')' to the stack.
3. After the scan is done, the stack will only contain the indices of characters which cannot be matched.
4. If the stack is empty at this point, the whole input string is valid.
Otherwise, we can scan the stack to get longest valid substring as described in step 3.

Time: O(n)
Space: O(n)
"""


def longest_valid_parentheses(s):
    if not s:
        return 0

    n, longest = len(s), 0

    stack = []

    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:  # current char must be ')'
            if stack:
                if s[stack[-1]] == '(':  # found a matching pair!
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

    # stack now contains indices of chars in s that could not be matched
    if not stack:  # if stack is empty as this point, this means all chars could be matched
        longest = n
    else:  # otherwise, we iterate through the stack to find longest valid substring
        start, end = 0, n
        while stack:
            start = stack[-1]
            stack.pop()
            longest = max(longest, end - start - 1)
            end = start

        longest = max(longest, end)

    return longest
