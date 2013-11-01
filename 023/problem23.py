#!/usr/bin/python

"""Problem 23: Non-abundant sums"""

from projecteuler import sum_of_proper_divisors

def main():
    MAX = 28123
    a_numbers = [ i for i in range(12, MAX+1) if sum_of_proper_divisors(i) > i ]
    a_numbers_set = frozenset(a_numbers)

    def not_sum(n):
        lim = n//2

        for a in a_numbers:
            if a > lim:
                break

            if n - a in a_numbers_set:
                return False

        return True

    return sum(filter(not_sum, range(MAX, 0, -1)))

if __name__ == "__main__":
    print(main())
