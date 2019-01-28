# coding=utf-8
# Solution to problem 41
# Problem Statement: Pandigital prime
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
#
#


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def is_prime(p):
    if p > 2:  # this will skip 2 as start from 3 as it will be neither a prime or composite
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:  # check if it is not a prime number
                return False
        return True


def pandigital_prime():
    n = "7654321"
    for i in xrange(len(n) + 1):
        p = all_perms(n[i:])
        for j in sorted(p, reverse=True):
            if is_prime(int(j)):
                return j


if __name__ == "__main__":
    print pandigital_prime()