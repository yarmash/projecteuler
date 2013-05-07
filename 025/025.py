#!/usr/bin/python2

a, b, c, term = 1, 1, 2, 3

while c < 10**999:
    a, b, c, term = b, c, b+c, term+1

print term
