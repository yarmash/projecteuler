#!/usr/bin/python2

from projecteuler import pythagorean_triplets

def main():
    s = p = 0

    for perimeter in xrange(12, 1001, 4): # the perimeter is always divisible by 4
        solutions = len(list(pythagorean_triplets(perimeter)))
        if solutions > s:
            s = solutions
            p = perimeter
    return p

if __name__ == "__main__":
    print main()
