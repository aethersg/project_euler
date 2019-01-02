# coding=utf-8
# Solution to problem 15
# Problem Statement: Lattice paths
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# ![image](images/p015.gif)
#
# How many such routes are there through a 20×20 grid?
#
# The issue is here is we could calculate the paths and store it however if we were to calculate it based
# on smaller historic values we can do it faster
#


def lattice_paths(n):
    cube = [1] * n
    for i in range(n):
        for j in range(i):
            cube[j] = cube[j] + cube[j - 1]
        cube[i] = 2 * cube[i - 1]
    return cube[n - 1]


if __name__ == "__main__":
    print lattice_paths(20)
