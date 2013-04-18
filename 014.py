#!/usr/bin/python2
# coding=utf-8

# The following iterative sequence is defined for the set of positive integers:

#    n → n/2 (n is even)
#    n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
#    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10
# terms. Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


cache = {}
longest = 0
num = 0

def get_chain_length(n):
    if n == 1:
        return 1
    if n in cache:
        return cache[n]

    cache[n] = length = 1 + get_chain_length(n/2 if n % 2 == 0 else 3*n+1)
    return length

for i in xrange(2, 1000000):
    length = get_chain_length(i)

    if length > longest:
        longest = length
        num = i

    i += 1

print num
