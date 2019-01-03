# coding=utf-8
# Solution to problem 16
# Problem Statement: Power digit sum
# ```
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# ```
#


def power_digit(n):
    try:
        n = int(n)
    except ValueError:
        return "This is not a valid integer"
    return sum([int(i) for i in str(2 ** n)])


if __name__ == "__main__":
    print power_digit(1000)
