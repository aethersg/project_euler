# coding=utf-8
# Solution to problem 43
# Problem Statement: Sub-string divisibility
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in
# some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
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


def prime_sieve(n):
    a = [True] * n
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, n, i):
                a[n] = False


def sub_string_divisibility():
    p = [int(i) for i in prime_sieve(18)]
    ans = []
    for i in all_perms("0123456789"):
        add = True
        for j in xrange(1, len(i) - 2, 1):
            if (int(i[j:j + 3]) % p[j - 1]) != 0:
                add = False
        if add:
            ans.append(int(i))
    return ans


if __name__ == "__main__":
    ans = sub_string_divisibility()
    print "The product sum is %s" % sum(ans)
