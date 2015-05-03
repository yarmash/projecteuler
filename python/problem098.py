#!/usr/bin/python

"""Problem 98: Anagramic squares"""

from math import ceil, sqrt
from collections import defaultdict
from itertools import combinations
from utils import open_data_file


def main():
    with open_data_file("words.txt") as data_file:
        words = data_file.read().replace('"', "").split(",")

    anagrams = defaultdict(lambda: defaultdict(list))

    for word in words:
        # skip palindromic words
        if word != word[::-1]:
            anagrams[len(word)]["".join(sorted(word))].append(word)

    answer = 0

    for length in sorted(anagrams, reverse=True):

        if any(len(x) > 1 for x in anagrams[length].values()):
            squares = {str(i*i) for i in range(ceil(sqrt(10**(length-1))),
                                               ceil(sqrt(10**length)))}
            for v in anagrams[length].values():
                if len(v) > 1:
                    for first, second in combinations(v, 2):
                        for square in squares:
                            mapping = {k: v for k, v in zip(first, square)}
                            rev = {v: k for k, v in mapping.items()}
                            if len(mapping) != len(rev) or "".join([
                                    rev.get(x, "") for x in square]) != first:
                                continue

                            other = "".join([mapping[x] for x in second])
                            if other in squares:
                                print(first, second, square, other)
                                answer = max(answer, int(square), int(other))
        if answer:
            return answer

if __name__ == "__main__":
    print(main())
