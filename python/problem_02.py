# Solution to problem 2
# Problem Statement: Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# The first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
#


def sum_of():
    ans = 0
    a = 1  # starting of the Fibonacci sequence
    b = 2  # next Fibonacci sequence number
    while a <= 4000000:  # while less then 4 million
        if a % 2 == 0:  # checking if even value
            ans += a
        a = b  # this become the b
        b = a + b  # this will be the calculated value where it is a+b
    print ans


if __name__ == "__main__":
    sum_of()
