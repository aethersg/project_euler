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


def is_pandigital(n):
    if len(n) > 9:
        return False

    for i in xrange(1, 10):
        if str(i) not in n:
            return False
    return True


def is_pandigital_product(x, y):
    ans = str(x) + str(y) + str(x * y)
    if len(ans) != 9:
        return False
    return is_pandigital(ans)


def pandigital_products():
    products = []
    for i in xrange(0, 100000):
        for j in xrange(i, 100000):
            if len(str(i * j) + str(i) + str(j)) > 9:
                break
            if is_pandigital_product(i, j):
                products.append(i * j)
                print("%i x %i = %i" % (i, j, i * j))
    return sum(set(products))


if __name__ == "__main__":
    print pandigital_products()
