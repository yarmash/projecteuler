#!/usr/bin/python2

"""Diophantine equation"""

# http://mathworld.wolfram.com/PellEquation.html
# http://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
# http://en.wikipedia.org/wiki/Continued_fraction#Pell.27s_equation


from math import sqrt
from projecteuler import sqrt_fraction_expansion, convergent_fractions


def quotients(n):
    f = sqrt_fraction_expansion(n)
    yield f.pop(0)

    while True:
        for i in f:
            yield i

def main():
    res, max_x = 0, 0

    for d in xrange(2, 1001):
        if sqrt(d).is_integer():
            continue

        for num, den in convergent_fractions(quotients(d)):
            if num*num - d*den*den == 1:
                if num > max_x:
                    max_x, res = num, d

                break
    return res

if __name__ == "__main__":
    print main()
