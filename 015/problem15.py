#!/usr/bin/python2

"""Problem 15: Lattice paths"""

from math import factorial

def main():
    n = 20
    return factorial(2*n)/(factorial(n)*factorial(n))

if __name__ == "__main__":
    print main()
