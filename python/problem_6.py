# coding=utf-8
# Solution to problem 6
# Problem Statement: Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
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
