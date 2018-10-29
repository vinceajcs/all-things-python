"""Given an integer, convert it to a roman numeral.

Time: O(n)
Space: O(1)
"""


def integer_to_roman(n):
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    result = []

    for i, num in enumerate(nums):
        while n >= num:
            result.append(romans[i])
            n -= num
        if n == 0:
            break

    return ''.join(result)
