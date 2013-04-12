#!/usr/bin/python2
# coding=utf-8

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13.
# What is the 10 001st prime number?

# Answer: 104743


from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True # we have already excluded 4, 6 and 8
    elif n % 3 == 0:
        return False
    else:
        limit = int(sqrt(n))
        k = 5
        while k <= limit: # check through all the numbers of the form 6k ± 1
            if n % k == 0:
                return False
            if n % (k+2) == 0:
                return False
            k += 6

        return True

x = 2
count = 0
while True:
    if is_prime(x):
        count += 1
        if count == 10001:
            break
    x += 1

print x
