#!/usr/bin/python

"""Problem 92: Square digit chains"""

from projecteuler import memoize

def main():

    @memoize
    def sum_squares(num):
        """Sums the squares of the digits in a number"""
        if num == 89 or num == 1:
            return num

        a, b, c = num // 100, (num % 100) // 10, num % 10
        return sum_squares(a*a + b*b + c*c)


    @memoize
    def count_numbers(n, k):
        """Calculate how many numbers have the sum of the squares equal to n"""
        if n < 0: return 0
        if n == k == 0: return 1
        if k == 0: return 0
        return sum([count_numbers(n - i*i, k - 1) for i in range(10)])

    return sum([count_numbers(num, 7) for num in range(2, 9**2*7+1) if sum_squares(num) == 89])

if __name__ == "__main__":
    print(main())
