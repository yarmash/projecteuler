#!/usr/bin/python2

"""Convergents of e"""


def main():
    # e = [2; 1,2,1, 1,4,1, 1,6,1, ...]
    def quotients():
        k = 2
        while True:
            yield 1
            yield k
            yield 1
            k += 2

    # http://en.wikipedia.org/wiki/Continued_fraction#Continued_fraction_expansions_of_.CF.80
    num, den, prev_num, prev_den = 2, 1, 1, 0
    quotient = quotients()
    cnt = 2

    while cnt <= 100:
        q = quotient.next()
        prev_num, num, prev_den, den = num, prev_num + num*q, den, prev_den + den*q
        cnt += 1

    return sum(map(int, str(num)))


if __name__ == "__main__":
    print main()
