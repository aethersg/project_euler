# coding=utf-8
# Solution to problem 42
# Problem Statement: Coded triangle numbers
#
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
# we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words, how many are triangle words?
#
#
# TODO: need to optimized


def coded_triangle_numbers():
    f = open("p042_words.txt", 'r')
    f = f.read().replace('"', '').split(',')
    lov = []
    for w in f:
        v = 0
        for c in w:
            v += ord(c) - 64
        lov.append(v)
    m = max(lov)
    triangle_value = []
    for i in range(1, 200):
        triv = int((0.5 * i) * (i + 1))
        if triv <= m:
            triangle_value.append(triv)
        else:
            break
    ans = 0
    for v in lov:
        if v in triangle_value:
            ans += 1
    return ans


if __name__ == "__main__":
    print coded_triangle_numbers()
