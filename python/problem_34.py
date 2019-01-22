# coding=utf-8
# Solution to problem 34
# Problem Statement: Digit factorials
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_digit_factorials():
    ans = []
    for i in xrange(10, 2540160):
        temp = 0
        for x in str(i):
            temp += factorial(int(x))
        if temp == i:
            ans.append(i)
    return sum(ans)


if __name__ == "__main__":
    print is_digit_factorials()
