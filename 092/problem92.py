#!/usr/bin/python

"""Problem 92: Square digit chains"""

from projecteuler import memoize
from itertools import combinations_with_replacement
from math import factorial


def main():
    @memoize
    def sum_squares(num):
        """Sums the squares of the digits in a number"""
        if num == 89 or num == 1 or num == 0:
            return num

        # the number is limited by 9^2*7 == 567
        a, b, c = num // 100, (num % 100) // 10, num % 10
        return sum_squares(a*a + b*b + c*c)

    factorials = [factorial(x) for x in range(8)]
    numbers = 0

    for digits in combinations_with_replacement(range(10), 7):
        if sum_squares(sum([x*x for x in digits])) == 89:
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
