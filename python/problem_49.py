# coding=utf-8
# Solution to problem 49
# Problem Statement: Prime permutations
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
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


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def prime_permutations():
    ps = []
    # get all primes which are 4 in length
    for p in prime_sieve(9999):
        if p > 1487:
            ps.append(p)
    # go through ps simple add 3330 to the value check if in ps.

    for p in ps:
        f = True
        if p + 3330 in ps:
            if p + 6660 in ps:
                ans = [p, p + 3330, p + 6660]
                perm = all_perms(str(ans[0]))
                for a in ans:
                    if str(a) not in perm:
                        f = False
                if f:
                    a = ""
                    for i in ans:
                        a += str(i)
                    return a


if __name__ == "__main__":
    print prime_permutations()
