#!/usr/bin/python

"""Problem 87: Prime power triples"""

from projecteuler import prime_sieve


def main():
    lim = 50000000
    lim_square = int(pow(lim-8-16, 1/2))
    lim_cube = int(pow(lim-4-16, 1/3))
    lim_fourth = int(pow(lim-4-8, 1/4))

    primes = prime_sieve(lim_square)

    squares = [pow(p, 2) for p in primes]
    cubes = [pow(p, 3) for p in primes if p <= lim_cube]
    fourths = [pow(p, 4) for p in primes if p <= lim_fourth]

    numbers = set([
        square + cube + fourth for square in squares
            for cube in cubes if square + cube < lim
            for fourth in fourths if square + cube + fourth < lim
    ])

    return len(numbers)

if __name__ == "__main__":
    print(main())
