#!/usr/bin/python

"""Problem 93: Arithmetic expressions"""

from itertools import product, combinations, permutations, zip_longest
from operator import add, sub, mul, truediv


def calc_consecutive(seq):
    """Return the number of consecutive integers 1 to n in the sequence"""
    last = seq[0]
    if last != 1:
        return 0

    for i in range(1, len(seq)):
        if seq[i] != last + 1:
            return last
        last += 1
    return last


def main():
    max_consecutive = 0
    answer = None
    operations = [add, sub, mul, truediv]

    for digits in combinations(range(1, 10), 4):
        perms = list(permutations(digits, 4))

        terms = []

        for perm in perms:
            for ops in product(operations, repeat=3):
                ops = ops[:4]

                term = []
                for pair in zip_longest(perm, ops):
                    if pair[1] is not None:
                        term.extend(pair)
                    else:
                        term.append(pair[0])
                terms.append(term)

        targets = set()

        # bracketify..
        for term in terms:
            first_op = term[1]
            second_op = term[3]
            third_op = term[5]

            # try some possible orders of operations
            # Note: these are not all possible orders (there're 3! == 6 of them)
            for tmp in (
                third_op(second_op(first_op(term[0], term[2]), term[4]), term[6]),
                second_op(first_op(term[0], term[2]), third_op(term[4], term[6])),
                third_op(first_op(term[0], second_op(term[2], term[4])), term[6])):

                if tmp > 0 and float(tmp).is_integer():
                    targets.add(int(tmp))

        cons = calc_consecutive(sorted(targets))
        if cons > max_consecutive:
            max_consecutive = cons
            answer = digits
    return "".join([str(d) for d in answer])

if __name__ == "__main__":
    assert calc_consecutive(range(2, 10)) == 0
    assert calc_consecutive(range(1, 10)) == 9
    assert calc_consecutive([1, 2, 3, 4, 6, 7, 8, 9]) == 4

    print(main())
