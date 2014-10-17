#!/usr/bin/python

"""Problem 92: Square digit chains"""

from projecteuler import memoize
from itertools import combinations_with_replacement
from math import factorial


def main():
    @memoize
    def sum_squares(num):
        """Sums the squares of the digits in a number"""
        if num == 1 or num == 89:
            return num
        s = 0
        while num:
            d = num % 10
            s += d*d
            num //= 10
        return sum_squares(s)

    factorials = [factorial(x) for x in range(8)]
    numbers = 0

    for digits in combinations_with_replacement(range(10), 7):

        number = digits[0]*1000000 + digits[1]*100000 + digits[2]*10000 + \
            digits[3]*1000 + digits[4]*100 + digits[5]*10 + digits[6]

        if number and sum_squares(number) == 89:
            counts = [0]*10
            for digit in digits:
                counts[digit] += 1

            permutations = factorials[7]
            for count in counts:
                if count > 1:
                    permutations //= factorials[count]
            numbers += permutations

    return numbers

if __name__ == "__main__":
    print(main())
