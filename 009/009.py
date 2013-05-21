#!/usr/bin/python2

from projecteuler import pythagorean_triplets

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
print reduce(lambda x, y: x*y, pythagorean_triplets(1000).next())
