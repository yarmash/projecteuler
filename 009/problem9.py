#!/usr/bin/python2

"""Problem 9: Special Pythagorean triplet"""

from projecteuler import pythagorean_triplets

def main():
    # There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    a, b, c = pythagorean_triplets(1000).next()
    return a*b*c

if __name__ == "__main__":
    print main()
