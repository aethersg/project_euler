# coding=utf-8
# Solution to problem 22
# Problem Statement: Names scores
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
#
#


def name_scores():
    f = open("p022_names.txt", 'r')
    m = {}
    c = 1
    for i in xrange(ord('A'), ord('Z') + 1):
        m[chr(i)] = c
        c += 1
    names = sorted(f.read().replace('"', '').split(','))
    count = 1
    ans = 0
    for name in names:
        temp = 0
        for c in name:
            temp += m.get(c)
        ans += count * temp
        count += 1
    return ans


if __name__ == "__main__":
    print name_scores()
