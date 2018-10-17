"""Idea: Convert list to integer.
1. Multiply each digit by proper place value and add to num.
2. Add 1 to integer, then convert back to list.

Time: O(n)
Space: O(1)
"""


def plus_one(digits):
    num = 0
    for i in range(len(digits)):
        power_of_ten = pow(10, len(digits - 1 - i))
        num += digits[i] * power_of_ten

    return [int(i) for i in str(num + 1)]
