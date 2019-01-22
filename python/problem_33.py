# coding=utf-8
# Solution to problem 33
# Problem Statement: Digit cancelling fractions
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing
# two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
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
