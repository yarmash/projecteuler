#!/usr/bin/python2
# coding=utf-8

# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99.  Find the largest palindrome made
# from the product of two 3-digit numbers.

# Answer: 906609


def reverse(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n /= 10
    return r

n = 0

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        k = x*y
        if k <= n:
            break

        if n < k and k == reverse(k):
            n = k
print(n)
