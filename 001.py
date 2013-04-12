#!/usr/bin/python2

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,
# 5, 6 and 9. The sum of these multiples is 23.  Find the sum of all the multiples of
# 3 or 5 below 1000.

# Answer: 233168


def SumDivisibleBy(n, limit):
    k = (limit - 1) / n
    sum = (n*(1+k)*k)/2
    return sum

limit = 1000

print( SumDivisibleBy(5, limit) + SumDivisibleBy(3, limit) - SumDivisibleBy(15, limit) )
