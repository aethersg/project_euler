# coding=utf-8
# Solution to problem 4
# Problem Statement: Largest palindrome product
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#


def palindrome():
    ans = 0
    for i in range(1000, 100, -1):  # loop through all 3 digits
        for j in range(1000, 100, -1):  # loop through all 3 digits
            n = str(i * j)
            if int(n) > ans:  # check the value is bigger then the previous one
                if n == n[::-1]:  # check if it is a palindrome
                    ans = int(n)  # if it is a palindrome and is bigger it becomes the answer
    return ans


if __name__ == "__main__":
    print palindrome()
