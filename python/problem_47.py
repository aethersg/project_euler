# coding=utf-8
# Solution to problem 47
# Problem Statement: Distinct primes factors
#
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?
#


def prime_factors(n):
    i = 2  # the starting prime number
    f = set()  # the array which will store the prime factors
    while i * i <= n:  # while the square root of the prime is smaller
        if n % i != 0:  # if the number can be modulus increment the value
            i += 1
        else:  # if n % i == 0 it will be a prime factor
            n //= i  # get the value of n after divided by i
            f.add(i)  # append the prime factor
    if n > 1:
        f.add(n)  # append the prime factor
    return f


def distinct_primes_factors():
    n = 2 * 3 * 5 * 7  # as this is the min value to start from where it is all primes
    c = 0
    while 1:
        if len(prime_factors(n)) == 4:
            c += 1
            if c == 4:
                return n
        else:
            c = 0
        n += 1


if __name__ == "__main__":
    n = distinct_primes_factors()
    print "The numbers are: %s %s %s %s" % (n - 3, n - 2, n - 1, n)
