#!/usr/bin/python2
# coding=utf-8

# Starting in the top left corner of a 2×2 grid, and only being able to move to the
# right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Answer: 137846528820


#from math import factorial
#n = 20
#print factorial(2*n)/(factorial(n)*factorial(n))


cache = {}

def count_routes(x, y):

    k = (x,y)

    if k in cache:
        return cache[k]

    if x == 0 and y == 0:
        n = 1
    else:
        n = 0
        if x > 0:
            n += count_routes(x-1, y)
        if y > 0:
            n += count_routes(x, y-1)

    cache[k] = n
    return n

print count_routes(20, 20)
