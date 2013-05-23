#!/usr/bin/python2

def pentagonal_numbers(n=1):
    while True:
        j = n*(3*n-1)/2
        yield j
        n += 1

def find_pair():
    pnumbers = set()

    for p in pentagonal_numbers():
        pnumbers.add(p)

        for p2 in pnumbers:
            if p - p2 in pnumbers and abs(2*p2 - p) in pnumbers:
                # I'm feeling lucky
                return abs(2*p2 - p)

print find_pair()
