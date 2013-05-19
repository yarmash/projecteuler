#!/usr/bin/python2

def sum_divisible_by(n, limit=1000):
    k = (limit - 1) / n
    s = (n*(1+k)*k)/2
    return s

print sum_divisible_by(5) + sum_divisible_by(3) - sum_divisible_by(15)
