# coding=utf-8
# Solution to problem 27
# Problem Statement: Quadratic primes
#
# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values 0 <= n <= 79.
# The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
#
# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.
#
#


def is_prime(p):  # reusing from problem 7
    if p >= 2:  # this will start from 2
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:  # check if it is not a prime number
                return False
        return True


def prime_sieve():
    a = [True] * 1000
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, 1000, i):
                a[n] = False


def count_consecutive_primes(a, b):
    n = 0
    t = n * n + a * n + b
    while is_prime(t):
        n += 1
        t = n * n + a * n + b
    return n


def quadratic_primes():
    max_c = 0
    max_a = 0
    max_b = 0
    primes = [int(i) for i in prime_sieve()]
    for a in range(-1000, 1000):
        for b in primes:
            c = count_consecutive_primes(a, b)
            if c > max_c:
                max_a, max_b, max_c = a, b, c
    return max_a, max_b, max_c


if __name__ == "__main__":
    a, b, c = quadratic_primes()
    print "a=%s b=%s the product=%s with consecutive of %s numbers" % (a, b, a * b, c)
