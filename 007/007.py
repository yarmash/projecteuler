#!/usr/bin/python2

from projecteuler import is_prime

x = 2
count = 0
while True:
    if is_prime(x):
        count += 1
        if count == 10001:
            break
    x += 1

print x
