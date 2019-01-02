# coding=utf-8
# Solution to problem 14
# Problem Statement: Longest Collatz sequence
#
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
#


def longest_collatz(n):
    max = [0, 0]
    try:
        n = int(n)
    except ValueError:
        return "This is not a valid number"

    for i in range(1, n):
        c = collatz(i)
        if c > max[0]:
            max[0] = c
            max[1] = i
    return "found %s at length %s " % (max[1], max[0])


def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count


if __name__ == "__main__":
    print longest_collatz(1000000)
