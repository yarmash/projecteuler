#!/usr/bin/env python3

"""Problem 59: XOR Decryption"""

from collections import Counter

from utils import get_path


def main():
    with get_path("data", "0059_cipher.txt").open() as data_file:
        codes = [int(code) for code in data_file.read().split(",")]

    # code frequency for each character of the key
    frequency = [Counter(codes[i::3]) for i in range(3)]

    # In English, the space (32) is the most frequent character
    key = [32 ^ max(f, key=f.get) for f in frequency]

    return sum([(k ^ key[i]) * v for i, f in enumerate(frequency)
                for k, v in f.items()])


if __name__ == "__main__":
    print(main())
