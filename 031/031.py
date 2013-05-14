#!/usr/bin/python2

from projecteuler import memoize

coins = [200, 100, 50, 20, 10, 5, 2, 1]

@memoize
def ways(amount, coin):

    if coin == 7 or amount == 0:
        return 1

    count = 0

    while amount >= 0:
        count += ways(amount, coin+1)
        amount -= coins[coin]
    return count

print ways(200, 0)
