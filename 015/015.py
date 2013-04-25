#!/usr/bin/python2

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
