# coding=utf-8
# Solution to problem 50
# Problem Statement: Consecutive prime sum
#
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
#
#


def prime_sieve(r):
    a = [True] * r
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, r, i):
                a[n] = False


def is_prime(p):
    if p > 2:  # this will skip 2 as start from 3 as it will be neither a prime or composite
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:  # check if it is not a prime number
                return False
        return True


def consecutive_prime_sum():
    ps = [p for p in prime_sieve(1000000)]
    max_sum = 0
    max_con = -1
    for i in xrange(len(ps)):
        sum = 0
        for j in xrange(i, len(ps)):
            sum += ps[j]
            if sum > 1000000:
                break
            if is_prime(sum) and sum > max_sum and j - i > max_con:
                max_con = j - i
                max_sum = sum
    return max_con, max_sum


if __name__ == "__main__":
    c, s = consecutive_prime_sum()
    print "The prime is %s and with consecutive of %s" % (s, c)
