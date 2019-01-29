# coding=utf-8
# Solution to problem 46
# Problem Statement: Goldbach's other conjecture
# ```
# It was proposed by Christian Goldbach that every odd composite number can be written as
# the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# ```
#


def is_prime(p):
    if p % 2 == 0:
        return False
    else:
        for i in xrange(3, int(p ** 0.5 + 1), 2):
            if p % i == 0:
                return False
        return True


def goldbach():
    n = 3
    p = [2]
    while 1:
        if is_prime(n):
            p.append(n)
        else:
            for i in p:
                if (((n - i) / 2) ** 0.5) == int(((n - i) / 2) ** 0.5):
                    break
            else:
                return n

        n += 2


if __name__ == "__main__":
    print goldbach()
