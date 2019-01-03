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
    #       jan feb mar apr may jun jul aug sep oct nov dec
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    leapyears = [year for year in range(1, 101) if year % 4 == 0]

    print leapyears


if __name__ == "__main__":
    print counting_sundays()
