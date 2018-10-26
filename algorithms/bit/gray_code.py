"""The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

Example:
Input: 2
Output: [0,1,3,2]

Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1

We can generate the sequence iteratively.
For example, when n = 3, we can get the solution based on n = 2.

00 01 11 10 -> 000 001 011 010

Then, we reverse the order!

000 001 011 010 -> 010 011 001 000

Finally, set the first bits to 1 (turn first bits on).

010 011 001 100 -> 110 111 101 100.

Combine the result with the result when n = 2.

00 01 11 10 110 111 101 100 -> [0, 2, 3, 1, 6, 7, 5, 4]

Time: O(n)
Space: O(1)
"""


def gray_code(n):
    result = [0]

    for i in range(n):
        for j in range(len(result) - 1, -1, -1):
            result.append(result[j] | 1 << i)

    return result
