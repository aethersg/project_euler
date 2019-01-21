# coding=utf-8
# Solution to problem 30
# Problem Statement: Digit fifth powers
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#


def digit_powers(n):
    ans = []
    for i in range(2, 355000):
        arr = []
        no = i
        while no > 0:
            d = int(no % 10)
            no /= 10
            arr.append(d ** n)
        if sum(arr) == i:
            ans.append(i)
    return ans


if __name__ == "__main__":
    ans = digit_powers(5)
    print "The number are %s and the sum of that result is %s" % (ans, sum(ans))
