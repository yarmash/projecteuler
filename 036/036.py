#!/usr/bin/python2

from projecteuler import is_palindrome

# generate palindromes in base 2
def palindromes(lim):
    i = 1

    while True:
        for n in (i>>1, i): # generate xyz+yx and xyz+zyx
            p = i
            while n:
                p = (p << 1) + (n & 1)
                n >>= 1
            if p >= lim: return
            yield p
        i += 1

lim = 1000000

print sum([ p for p in palindromes(lim) if is_palindrome(p, 10) ]);
