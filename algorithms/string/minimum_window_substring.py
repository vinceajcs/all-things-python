"""Given a string s and a string t, find the minimum window in s which will contain all the characters in t.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Note:
If there is no such window in s that covers all characters in t, return the empty string.
If there is such window, you are guaranteed that there will always be only one unique minimum window in t.

Idea: A window is desirable if it has all the chars from t.
We can use two pointers, left and right, where right is used to expand a window and left to contract.

1. Find the first window that contains all letters in t (desirable window).
2. Keep expanding the window to the right by 1 char at a time, reducing the window with the left pointer if possible.
Ensure that the active window is always desirable. In this case, every time the window is expanded, only the new char needs to be checked.

Time: O(s+t)
Space: O(s+t)
"""


def minimum_window_substring(s, t):
    need, missing = collections.Counter(t), len(t)

    """Note that i and j are the left and right pointers metioned in the idea;
    it is used to keep track of a current window.
    """

    start, end, i = 0, 0, 0

    for j, char in enumerate(s, 1):  # index j (right pointer) starts from 1
        # we found a char that we want in the desirable window
        if need[char] > 0:
            missing -= 1

        """Here, we update the value of need[char].
        If need[char] is negative, that means the char is not in the desired window.
        This is what the if condition checks for above.
        """
        need[char] -= 1

        # we found a desirable window!
        if missing == 0:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1

            need[s[i]] += 1
            missing += 1

            # update min window
            if end == 0 or j - i < end - start:
                start, end = i, j

            i += 1  # update left pointer for next active window

    return s[start:end]


"""Another idea:
1. Have both left and right pointers start at beginning of string.
2. Expand window with right pointer until we get a desirable window.
3. Once we have a desirable window, move left pointer by one (contract window).
If the window is still desirable, update min window size and move left pointer again.
4. If window is no longer desirable, repeat step 2 and onwards.
"""


def minimum_sliding_window(s, t):
    need, missing = collections.Counter(t), len(t)

    # start and end are our left and right pointers; head is used to record start of substring that we return
    start, end, head = 0, 0, 0
    min_substring_length = float('inf')

    while end < len(s):
        # we found a char that we want in the desirable window
        if need[s[end]] > 0:
            missing -= 1

        """Here, we update the value of need[s[end]].
        If need[s[end]] is zero or negative, that means the char s[end] is not in the desired window.
        This is what the if condition checks for above.
        """
        need[s[end]] -= 1

        # move right pointer to search for a desirable window
        end += 1

        # we found a desirable window!
        while missing == 0:
            # update min window
            if (end - start) < min_substring_length:
                min_substring_length = end - start
                head = start

            # check if we would still have a desired window were we to move the left pointer
            need[s[start]] += 1
            """If need[s[start]] is > 0, that means we would no longer have a desirable window were we to move the left pointer.
            This is because we would be missing the first character of our substring, which was needed to form the desirable window.
            """
            if need[s[start]] > 0:
                missing += 1

            start += 1  # move left pointer (contract window)

    return "" if min_substring_length == float('inf') else s[head:head + min_substring_length]
