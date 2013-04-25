#!/usr/bin/python2

def SumDivisibleBy(n, limit):
    k = (limit - 1) / n
    sum = (n*(1+k)*k)/2
    return sum

limit = 1000

print( SumDivisibleBy(5, limit) + SumDivisibleBy(3, limit) - SumDivisibleBy(15, limit) )
