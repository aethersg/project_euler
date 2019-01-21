# coding=utf-8
# Solution to problem 32
# Problem Statement: Pandigital products
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
# multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#
#


def pandigital_products():
    change = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (change + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], change + 1):
            ways[j] += ways[j - coins[i]]
    return max(ways)


if __name__ == "__main__":
    print pandigital_products()
