"""Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Example 1:
Input: ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]


Time: O(n)
Space: O(1)
"""


def compress(chars):
    left = i = 0

    while i < len(chars):
        char, length = chars[i], 1

        # get frequency of char to be compressed
        while (i + 1) < len(chars) and char == chars[i + 1]:
            length += 1
            i += 1

        chars[left] = char

        # compress by modifying original array char
        if length > 1:
            str_len = str(length)
            chars[left + 1:left + 1 + len(str_len)] = str_len
            left += len(str_len)

        left += 1
        i += 1

    return left
