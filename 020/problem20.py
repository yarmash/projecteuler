#!/usr/bin/python2

from math import factorial

def main():
    return sum(int(d) for d in str(factorial(100)))

if __name__ == "__main__":
    print main()
