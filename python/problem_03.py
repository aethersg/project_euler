# Solution to problem 3
# Problem Statement: Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#


def prime_factors(n):
    i = 2  # the starting prime number
    f = []  # the array which will store the prime factors
    while i * i <= n:  # while the square root of the prime is smaller
        if n % i != 0:  # if the number can be modulus increment the value
            i += 1
        else:  # if n % i == 0 it will be a prime factor
            n //= i  # get the value of n after divided by i
            f.append(i)  # append the prime factor
    if n > 1:
        f.append(n)  # append the prime factor
    return f


if __name__ == "__main__":
    f = prime_factors(int(raw_input("Please Enter the Number which you will want the prime Factors: ")))
    print "The Largest prime factor is : " + str(max(f))
    print "The prime factors are : " + " ".join(str(i) for i in f)
