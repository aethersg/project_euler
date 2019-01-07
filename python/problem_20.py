# coding=utf-8
# Solution to problem 20
# Problem Statement: Factorial digit sum
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
#
#


def factorial_digit_sum(n):
    ans = 1
    for i in range(n, 0, -1):
        ans *= i
    return sum([int(i) for i in str(ans)])


if __name__ == "__main__":
    print factorial_digit_sum(100)
