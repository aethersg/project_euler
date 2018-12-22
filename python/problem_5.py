# coding=utf-8
# Solution to problem 5
# Problem Statement: Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#


def least_common_multiple():
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:   # find the values with remainder
            for j in range(1, 21):
                if (i * j) % k == 0:    # get the value of i*k which has no remainder
                    i *= j  # create the new value which can be divided by all value in range.
                    break
    return i


if __name__ == "__main__":
    print least_common_multiple()
