#!/usr/bin/python2

from projecteuler import nth_triangle, nth_square, nth_pentagonal, nth_hexagonal, nth_heptagonal, nth_octagonal
from operator import itemgetter


def is_cyclic(m, n):
    return m % 100 == n / 100

def main():
    numbers = [ # the ranges can be figured out using the respective formulas
        map(nth_triangle, xrange(45, 141)), # 4-digit triangle numbers
        map(nth_square, xrange(31, 100)), # 4-digit square numbers
        map(nth_pentagonal, xrange(25, 82)),
        map(nth_hexagonal, xrange(22, 71)),
        map(nth_heptagonal, xrange(20, 64)),
        map(nth_octagonal, xrange(18, 59))
    ]


    def get_number(n):
        return numbers[n[0]][n[1]]

    types = set(range(6))
    typegetter = itemgetter(0)


    def search(n):
        if len(n) == 6:
            if is_cyclic(*map(get_number, (n[-1], n[0]))):
                return n
            return

        unused_types = types - set(map(typegetter, n))
        this_num = get_number(n[-1])

        for u in unused_types:
            for k in xrange(len(numbers[u])):
                if is_cyclic(this_num, numbers[u][k]):
                    s = search(n+[(u, k)])
                    if s: return s

    for i in xrange(len(numbers[5])): # start from the octagonal numbers
        s = search([(5, i)])
        if s: return sum(map(get_number, s))


if __name__ == "__main__":
    print main()
