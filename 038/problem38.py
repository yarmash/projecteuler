#!/usr/bin/python2

from projecteuler import is_pandigital
from itertools import permutations

def main():
    # the number can have 4 digits max since the concatenated product has the length 9
    for i in range(4, 0, -1):
        for p in permutations("987654321", i):
            p = "".join(p)
            k = int(p) << 1   # initial product (number*2)
            c = p+str(k)      # the concatenated product

            while len(c) <= 9:
                if is_pandigital(int(c)):
                    return c
                k += int(p)
                c += str(k)

if __name__ == "__main__":
    print main()
