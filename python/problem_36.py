# coding=utf-8
# Solution to problem 36
# Problem Statement: Double-base palindromes
#
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#
#


def get_palindrome_b10(n):
    arr = []
    for i in xrange(10, n + 1):
        temp = str(i)
        if temp == temp[::-1]:
            arr.append(i)
    return arr


def get_palindrome_b2(pb):
    c = 0
    for n in pb:
        temp = str(bin(n)[2:])
        if temp == temp[::-1]:
            c += n
    return c


if __name__ == "__main__":
    p = get_palindrome_b10(1000000)
    print get_palindrome_b2(p)
