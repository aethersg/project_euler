# coding=utf-8
# Solution to problem 10
# Problem Statement: Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
#


def is_prime(p):  # reusing from problem 7
    if p >= 2:  # this will start from 2
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:  # check if it is not a prime number
                return False
        return True


def sum_of_primes(v):
    ps = [] # array of primes
    for i in range(2, v):
        if is_prime(i):
            ps.append(i)
    return ps, sum(ps) # returns the array of primes and the sum of the array


if __name__ == "__main__":
    ps, sp = sum_of_primes(2000000)
    print "The primes are : " + ",".join(str(i) for i in ps)
    print "The sum of the primes are :" + str(sp)
