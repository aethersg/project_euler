# coding=utf-8
# Solution to problem 40
# Problem Statement: Champernowne's constant
#
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
#
# TODO: this is not optimized


def champernowne():
    nd = 0
    f = [1, 10, 100, 1000, 10000, 100000, 1000000]
    cn = []
    for i in range(1, 200000):
        for d in str(i):
            nd += 1
            if nd in f:
                cn.append(int(d))
    return reduce(lambda x, y: x * y, cn)


if __name__ == "__main__":
    print champernowne()
