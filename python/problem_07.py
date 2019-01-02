# coding=utf-8
# Solution to problem 7
# Problem Statement: 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?
#


def is_prime(p):
    if p > 2:  # this will skip 2 as start from 3 as it will be neither a prime or composite
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:  # check if it is not a prime number
                return False
        return True


def nth_prime():
    no_of_prime = 0
    prime = 1

    while no_of_prime < 10000:
        prime += 1
        if is_prime(prime):
            no_of_prime += 1
    return prime


if __name__ == "__main__":
    print nth_prime()
