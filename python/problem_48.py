# coding=utf-8
# Solution to problem 48
# Problem Statement: Self powers
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
#
# TODO: need to optimized

def self_powers(n):
    ans = 0
    for i in xrange(1, n + 1):
        ans += i ** i
    return str(ans)[-10:]


if __name__ == "__main__":
    print self_powers(1000)
