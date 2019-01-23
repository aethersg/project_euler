# coding=utf-8
# Solution to problem 35
# Problem Statement: Circular primes
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
# are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
#


def prime_sieve(r):
    a = [True] * r
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, r, i):
                a[n] = False


def is_circular_prime(p, n):
    n = str(n)
    for i in xrange(len(n)):
        rn = n[i:len(n)] + n[0:i]
        if int(rn) not in p:
            return False
    return True


def circular_prime(n):
    c = 0
    not_prime = ['0', '2', '4', '5', '6', '8']
    ps = [int(i) for i in prime_sieve(n)]
    for p in ps:
        for i in not_prime:
            if i in str(p):
                continue
        if is_circular_prime(ps, p):
            c += 1
    return c


if __name__ == "__main__":
    print circular_prime(1000000)
