#!/usr/bin/python2
# coding=utf-8

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#    a² + b² = c²

# For example, 3² + 4² = 9 + 16 = 25 = 5².

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Answer: 31875000


s = 1000

for n in xrange(1, 1000):
    for m in xrange(n+1, 1000):
        k = 1
        while True:
            a = k*(m**2 - n**2)
            b = k*(2*m*n)
            c = k*(m**2 + n**2)

            if a+b+c > s:
                break

            if a+b+c == s:
                print a*b*c
                exit()

            k += 1
