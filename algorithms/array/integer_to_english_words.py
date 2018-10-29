"""Convert a non-negative integer to its English words representation.

Time: O(n)
Space: O(1)
"""


to19 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]


def numberToWords(n):
    if n == 0:
        return 'Zero'

    result = ''

    for i in range(len(thousands)):
        if n % 1000 != 0:
            result = helper(n % 1000) + thousands[i] + ' ' + result
        n //= 1000

    return result.strip()


def helper(n):
    if n == 0:
        return ''
    elif n < 20:
        return to19[n] + ' '
    elif n < 100:
        return tens[n // 10] + ' ' + helper(n % 10)
    else:
        return to19[n // 100] + ' Hundred ' + helper(n % 100)
