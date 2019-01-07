# coding=utf-8
# Solution to problem 17
# Problem Statement: Counting Sundays
#
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
#


def counting_sundays():
    # given 1,1,1901 ==> tues 6,1,1901 ==> sunday
    ans = 0
    start_date = [6, 1, 1901]
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while start_date[2] != 2001:
        if start_date[2] % 4 == 0 and (start_date[2] % 100 != 0 or start_date[2] % 400 == 0):
            month[1] = 29
        else:
            month[1] = 28

        start_date[0] += 7

        if start_date[0] > month[start_date[1] - 1]:
            start_date[0] = start_date[0] - month[start_date[1] - 1]
            start_date[1] += 1
            if start_date[1] > 12:
                start_date[1] = start_date[1] % 12
                start_date[2] += 1
        if start_date[0] == 1:
            ans += 1
    return ans


if __name__ == "__main__":
    print counting_sundays()
