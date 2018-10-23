"""Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight)."""


def hamming_weight(n):
    return bin(n).count('1')


def hamming_weight(n):
    count = 0
    while n:
        # cancel a 1 bit at each iteration
        n &= n - 1
        count += 1
    return count
