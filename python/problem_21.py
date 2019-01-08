# coding=utf-8
# Solution to problem 21
# Problem Statement: Amicable numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
#
#
#


def amicable_numbers(n):
    ans = set()
    for i in xrange(1, n):
        an = proper_divisors(i)
        if an == proper_divisors(i) and proper_divisors(an) == i and i != an:
            ans.add(an)
            ans.add(i)
    return sum(ans)


def proper_divisors(n):
    ans = []
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)
    return sum(ans)


if __name__ == "__main__":
    print amicable_numbers(10000)
