#!/usr/bin/python2

from projecteuler import prime_sieve

p = prime_sieve(65500)
t = 1
s = 1
cnt = 0

while cnt <= 500:
    cnt = 1
    s += 1
    t += s
    tt = t

    for i in p:
        if i**2 > tt:
            cnt *= 2
            break
        exponent = 1
        while tt % i == 0:
            exponent += 1
            tt /= i
        if exponent > 1:
            cnt *= exponent
        if tt == 1:
            break
print t
