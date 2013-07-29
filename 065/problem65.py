#!/usr/bin/python2

"""Convergents of e"""

from projecteuler import convergent_fractions


def main():
    # e = [2; 1,2,1, 1,4,1, 1,6,1, ...]
    def quotients():
        yield 2

        k = 2
        while True:
            yield 1
            yield k
            yield 1
            k += 2

    convergents = convergent_fractions(quotients())

    for i in xrange(100):
        num = convergents.next()[0]

    return sum(map(int, str(num)))


if __name__ == "__main__":
    print main()
