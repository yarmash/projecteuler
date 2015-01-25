#!/usr/bin/python

"""Problem 59: XOR decryption"""

from collections import defaultdict
from projecteuler import data_file


def main():
    with open(data_file("cipher1.txt")) as data:
        codes = eval(data.read())

    # code frequency for each character of the key
    frequency = [defaultdict(int) for i in range(3)]

    for i, code in enumerate(codes):
        frequency[i % 3][code] += 1

    # In English, the space (32) is the most frequent character
    key = [32^max(f.keys(), key=f.get) for f in frequency]

    return sum((k^key[i])*v for i, f in enumerate(frequency) for k, v in f.items())

if __name__ == "__main__":
    print(main())
