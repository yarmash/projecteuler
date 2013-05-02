#!/usr/bin/python2

#from math import factorial
#n = 20
#print factorial(2*n)/(factorial(n)*factorial(n))

from projecteuler import memoize

@memoize
def count_routes(x, y):
    if x == 0 and y == 0:
        n = 1
    else:
        n = 0
        if x > 0:
            n += count_routes(x-1, y)
        if y > 0:
            n += count_routes(x, y-1)

    return n

print count_routes(20, 20)
