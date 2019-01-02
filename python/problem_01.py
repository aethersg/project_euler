# Solution to problem 1
# Problem Statement: Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#


def sum_of(a):
    # try to convert the value input as an integer if failed tell user failed.
    # if not it will calculate the sum of the value in the range.
    try:
        a = int(a)
    except ValueError:
        return "Sorry this is not an integer value"
    return sum(i for i in range(a) if (i % 3 == 0 or i % 5 == 0))


if __name__ == "__main__":
    r = raw_input("Please enter range: ")
    print sum_of(r)
