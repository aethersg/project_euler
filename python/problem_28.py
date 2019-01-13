# coding=utf-8
# Solution to problem 28
# Problem Statement: Number spiral diagonals
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
#


def spiral_diagonals(n):
    n = (n - 1) / 2
    return 2 * n * (8 * n * n + 15 * n + 13) / 3 + 1


if __name__ == "__main__":
    print spiral_diagonals(101)
