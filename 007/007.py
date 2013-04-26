#!/usr/bin/python2

from projecteuler import is_prime

x = 3
count = 2

while count < 10001:
    x += 2 # loop through odd numbers
    if is_prime(x):
        count += 1

print x
