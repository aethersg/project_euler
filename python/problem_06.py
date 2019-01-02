# coding=utf-8
# Solution to problem 6
# Problem Statement: Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#


def sum_square_difference():
    r = range(1, 101)  # the range of the natural number
    sum_of_square = sum([i ** 2 for i in r])
    square_of_sum = sum(r) ** 2
    return square_of_sum - sum_of_square


if __name__ == "__main__":
    print sum_square_difference()
