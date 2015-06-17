#!/usr/bin/python

"""Problem 103: Special subset sums: optimum"""

from itertools import combinations, chain


def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def main():
    candidates = []

    # make an educated guess about limits, based on the problem definition
    for A in combinations(range(30, 47), 6):
        A = (20,) + A

        for B, C in combinations(powerset(A), 2):
            sb = sum(B)
            sc = sum(C)
            if sb == sc:
                break

            if len(B) > len(C):
                if sb < sc:
                    break
            elif len(B) < len(C):
                if sb > sc:
                    break
        else:
            candidates.append(A)

    return "".join([str(x) for x in min(candidates, key=sum)])

if __name__ == "__main__":
    print(main())
