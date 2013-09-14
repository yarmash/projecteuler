#!/usr/bin/python2

"""Counting fractions"""

# http://en.wikipedia.org/wiki/Farey_sequence
def main():
    lim = 1000000

    phis = range(lim+1)

    for i in xrange(2, lim+1):
        if phis[i] == i: # i is a prime
            for j in xrange(i, lim+1, i):
                phis[j] -= phis[j]/i

    return sum(phis) - 1


if __name__ == "__main__":
    print main()
