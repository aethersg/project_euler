# coding=utf-8
# Solution to problem 39
# Problem Statement: Integer right triangles
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
#


def int_right_tri(n):
    pm, sol = 0, 0
    for p in range(2, n + 1, 2):
        nosol = 0
        a = 2
        while a < (p / 3):
            if (p * (p - 2 * a) % (2 * (p - a))) == 0:
                nosol += 1
            a += 1
        if nosol > sol:
            sol = nosol
            pm = p
    return pm, sol


if __name__ == "__main__":
    p, sol = int_right_tri(1000)
    print "The maximum parameter is %s where there are %s solutions" % (p, sol)
