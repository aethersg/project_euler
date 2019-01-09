# coding=utf-8
# Solution to problem 23
# Problem Statement: Non-abundant sums
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and
# it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
# as the sum of two abundant numbers is 24.
# By mathematical analysis,
# it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is
# known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
# 4179871
#


def is_abundant(n):
    sum = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            sum += i
    return sum > n


def non_abundant_sums(n):
    ans = [x for x in range(1, n) if is_abundant(x)]
    l = range(n)
    for x in ans:
        for y in ans:
            if x + y >= n:
                break
            l[x + y] = 0
    return sum(l)


if __name__ == "__main__":
    print non_abundant_sums(28123)
