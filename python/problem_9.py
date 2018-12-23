# coding=utf-8
# Solution to problem 9
# Problem Statement: Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#  a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
#
#


def pythagorean_triplet():
    parameter = 1000  # parameter which is needed
    for a in range(1, parameter):  # range of the value a
        for b in range(a + 1, parameter):  # range of value b
            c = a ** 2 + b ** 2
            c = c ** 0.5
            if (a + b + c) == parameter:  # if the parameter is equal to the parameter we return the value
                return a * b * c


if __name__ == "__main__":
    print pythagorean_triplet()
