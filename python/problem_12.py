# coding=utf-8
# Solution to problem 12
# Problem Statement: Highly divisible triangular number
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1 3: 1,3 6: 1,2,3,6 10: 1,2,5,10 15: 1,3,5,15 21: 1,3,7,21 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?
#
#


def triangular_number():
    fa = 0
    ans = 0
    while fa < 500:
        ans += 1
        tri = sum(range(1, ans + 1))
        fa = factors(tri)
    return tri


def factors(f):
    factor_array = 0
    i = 1
    while i <= f ** 0.5:
        if f % i == 0:
            factor_array += 1
        i += 1
    factor_array *= 2
    return factor_array


if __name__ == "__main__":
    print triangular_number()
