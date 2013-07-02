#!/usr/bin/python2

"""Problem 59: XOR decryption"""

import os

def main():
    datafile = os.path.join(os.path.dirname(__file__), "cipher1.txt")
    codes = eval(open(datafile).read())

    frequency = [{}, {}, {}] # code frequency for each character of the key

    for i, code in enumerate(codes):
        frequency[i%3][code] = frequency[i%3].get(code, 0) + 1

    # In English, the space (32) is the most frequent character
    key = map(lambda f: 32^max(f.keys(), key=lambda x: f[x]), frequency)

    return sum((k^key[i])*v for i, f in enumerate(frequency) for k, v in f.iteritems())

if __name__ == "__main__":
    print main()
