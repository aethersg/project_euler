# coding=utf-8
# Solution to problem 17
# Problem Statement: Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
# there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
#
#
m = {1: 'one',
     2: 'two',
     3: 'three',
     4: 'four',
     5: 'five',
     6: 'six',
     7: 'seven',
     8: 'eight',
     9: 'nine',
     10: 'ten',
     11: 'eleven',
     12: 'twelve',
     13: 'thirteen',
     14: 'fourteen',
     15: 'fifteen',
     16: 'sixteen',
     17: 'seventeen',
     18: 'eighteen',
     19: 'nineteen',
     20: 'twenty',
     30: 'thirty',
     40: 'forty',
     50: 'fifty',
     60: 'sixty',
     70: 'seventy',
     80: 'eighty',
     90: 'ninety',
     100: 'hundred',
     1000: 'thousand',
     }


def number_letter_count(n):
    count = 0
    for i in range(1, n + 1):
        if i < 20:
            count += len(m.get(i))
        elif 20 <= i <= 99:
            a = int(str(i)[0] + '0')
            b = int(str(i)[1])
            if b != 0:
                count += (len(m.get(a)) + len(m.get(b)))
            else:
                count += len(m.get(a))
        elif 99 < i <= 999:
            a = int(str(i)[0] + '00')
            b = int(str(i)[1] + '0')
            c = int(str(i)[2])
            if (b + c) < 20:
                if b + c == 0:
                    count += (len(m.get(int(str(a)[0]))) + len(m.get(100)))
                else:
                    count += (len(m.get(int(str(a)[0]))) + len(m.get(100)) + len(m.get(b + c)) + 3)
            else:
                if b != 0 and c != 0:
                    count += (len(m.get(int(str(a)[0]))) + len(m.get(100)) + len(m.get(b)) + len(m.get(c)) + 3)
                if b == 0 and c != 0:
                    count += (len(m.get(int(str(a)[0]))) + len(m.get(100)) + len(m.get(c)) + 3)
                if b != 0 and c == 0:
                    count += (len(m.get(int(str(a)[0]))) + len(m.get(100)) + len(m.get(b)) + 3)
                if b == 0 and c == 0:
                    count += (len(m.get(int(str(a)[0]))) + len(m.get(100)))
        elif i == 1000:
            count += 11
    return count


if __name__ == "__main__":
    print number_letter_count(1000)
