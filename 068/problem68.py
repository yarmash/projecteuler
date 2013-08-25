#!/usr/bin/python2

"""Magic 5-gon ring"""

from itertools import permutations
from operator import itemgetter


def main():
    def rings():
        seen = set()
        getters = map(lambda i: itemgetter(*i), ((0, 1, 2), (3, 2, 4), (5, 4, 6), (7, 6, 8), (9, 8, 1)))

        for perm in permutations(range(1, 10)):
            # 10 must be in one of the outer nodes since the answer is 16-digit
            perm = (10,) + perm

            lines = tuple(map(lambda getter: tuple(getter(perm)), getters))

            if all(sum(l) == sum(lines[0]) for l in lines[1:]):
                lowest = min(lines, key=itemgetter(0))
                idx = lines.index(lowest)
                ring = lines[idx:] + lines[:idx]

                if not ring in seen:
                    yield ring
                    seen.add(ring)

    return max(map(int, map(lambda ring: "".join(map(lambda line: "".join(map(str, line)), ring)), rings())))


if __name__ == "__main__":
    print main()
