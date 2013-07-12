#!/usr/bin/python2

"""Convergents of e"""

from fractions import Fraction


def main():
    # e = [2; 1,2,1, 1,4,1, 1,6,1 ...]
    def quotients():
        k = 2
        while True:
            yield 1
            yield k
            yield 1
            k += 2

    def reciprocal(cnt=1):
        cnt += 1

        if cnt == lim:
            return Fraction(1, q.next())

        return Fraction(1, q.next() + reciprocal(cnt))

    lim = 100
    q = quotients()
    res = 2+reciprocal()
    return sum(map(int, str(res.numerator)))


if __name__ == "__main__":
    print main()
