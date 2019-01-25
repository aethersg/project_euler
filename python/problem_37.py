# coding=utf-8
# Solution to problem 37
# Problem Statement: Truncatable primes
#
# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
    if p > 1:  # this will skip 2 as start from 3 as it will be neither a prime or composite
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:  # check if it is not a prime number
                return False
        return True
    else:
        return False


def is_truncatable(p):
    div = 10
    while div < p:
        if (not is_prime(p % div)) or (not is_prime(p / div | 0)):
            return False
        div *= 10
    return True


def truncatable_prime():
    ans = []
    ps = [i for i in prime_sieve(1000000)]
    for p in ps:
        if is_truncatable(p) and p > 7:
            ans.append(p)
        if len(ans) == 11:
            break
    return sum(ans)


if __name__ == "__main__":
    print truncatable_prime()
