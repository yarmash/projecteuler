#!/usr/bin/python

"""Problem 96: Su Doku"""

from utils import open_data_file
from itertools import combinations, product, chain
from collections import defaultdict

numbers = set("123456789")

peers = {}
units = {}

for row in range(9):
    for col in range(9):

        # Every square has 3 units and 20 peers
        peers[(row, col)] = set(chain(
            [(row, c) for c in range(9) if c != col],
            [(r, col) for r in range(9) if r != row],
            [(r, c) for r in range(row//3*3, row//3*3+3)
             for c in range(col//3*3, col//3*3+3) if r != row or c != col]))

        units[(row, col)] = (
            [(row, c) for c in range(9) if c != col],
            [(r, col) for r in range(9) if r != row],
            [(r, c) for r in range(row//3*3, row//3*3+3)
             for c in range(col//3*3, col//3*3+3) if r != row or c != col])


def verify_grid(grid):
    for (row, col), unts in units.items():
        assert len(grid[row][col]) == 1
        for u in unts:
            assert set([x for r, c in u for x in grid[r][c]]) | set(grid[row][col]) == numbers


def eliminate(candidates, row, col, value):
    if value not in candidates[row][col]:
        return

    candidates[row][col].remove(value)

    if len(candidates[row][col]) == 1:
        # no easy way to get a value from a set w/o removing it
        for v in candidates[row][col]:
            for r, c in peers[(row, col)]:
                    eliminate(candidates, r, c, v)


def assign(candidates, row, col, value):
    other_values = candidates[row][col] - {value}

    for v in other_values:
        eliminate(candidates, row, col, v)


def solve_puzzle(grid):
    """Solve the puzzle and return the 3-digit number found in the top left
    corner of the solution grid"""
    candidates = [[set(numbers) for row in range(9)] for col in range(9)]

    for row in range(9):
        for col in range(9):
            if grid[row][col] != "0":
                assign(candidates, row, col, grid[row][col])

    while not all(len(x) == 1 for row in candidates for x in row):

        # check single-square candidates within an area (row/column/box)
        assigned = 1
        while assigned:
            assigned = 0
            for (row, col), unts in units.items():
                if len(candidates[row][col]) > 1:
                    for v in candidates[row][col]:
                        for u in unts:
                            if all(v not in candidates[r][c] for r, c in u):
                                assign(candidates, row, col, v)
                                assigned += 1
                                break
                        else:
                            continue
                        break

        # search for disjoint subsets, aka naked pairs/triples/etc.
        # pairs
        for row, col in product(range(9), repeat=2):
            if len(candidates[row][col]) == 2:
                for u in units[(row, col)]:
                    if any(candidates[r][c] == candidates[row][col] for r, c in u):
                        for r, c in u:
                            if candidates[r][c] != candidates[row][col]:
                                for v in set(candidates[row][col]):
                                    eliminate(candidates, r, c, v)
        # triples
        for (row, col), unts in units.items():
            # check if this square forms a 'disjoint subset' with others
            for u in unts:
                for others in combinations(u, 2):
                    if all(len(candidates[r][c]) == 1 for r, c in others):
                        continue
                    s = set(candidates[row][col])

                    for r, c in others:
                        s |= candidates[r][c]
                        if len(s) > 3:
                            break
                    else:
                        if len(s) == 3:
                            for r, c in u:
                                if not (r, c) in others:
                                    for v in s:
                                        eliminate(candidates, r, c, v)

        # x-wings
        # When there are
        # * only two possible cells for a value in each of two different rows,
        # * and these candidates lie also in the same columns,
        # then all other candidates for this value in the columns can be eliminated.

        wings = {c: defaultdict(list) for c in numbers}

        for row in range(9):
            for c in numbers:
                indexes = [col for col in range(9) if c in candidates[row][col]]

                if len(indexes) == 2:
                    wings[c][tuple(indexes)].append(row)

        for num, data in wings.items():
            for k, v in data.items():
                if len(v) != 2:
                    continue

                for r in [x for x in range(9) if x not in v]:
                    for col in k:
                        eliminate(candidates, r, col, num)

        # box line reduction
        # If all occurrences of a candidate within a row or column fall inside
        # the same box, then other occurrences of that candidate can be removed
        # from that box
        for row in range(9):
            for num in numbers:
                occurrences = {col for col in range(9) if num in candidates[row][col]}

                if len(occurrences) > 1:
                    if occurrences < set(range(3)) or occurrences < set(range(3, 6)) or occurrences < set(range(6, 9)):
                        others = {x for col in occurrences for x in units[(row, col)][2]} - set([(row, col) for col in occurrences])
                        for r, c in others:
                            eliminate(candidates, r, c, num)
        for col in range(9):
            for num in numbers:
                occurrences = {row for row in range(9) if num in candidates[row][col]}

                if len(occurrences) > 1:
                    if occurrences < set(range(3)) or occurrences < set(range(3, 6)) or occurrences < set(range(6, 9)):
                        others = {x for row in occurrences for x in units[(row, col)][2]} - set([(row, col) for row in occurrences])
                        for r, c in others:
                            eliminate(candidates, r, c, num)

    return int("".join(chain(*candidates[0][:3])))


def main():
    nsum = 0

    with open_data_file("sudoku.txt") as data_file:
        grid = []

        for i, line in enumerate(data_file):
            if i % 10:
                grid.append(line.rstrip())

                if len(grid) == 9:
                    nsum += solve_puzzle(grid)
                    grid *= 0
    return nsum

if __name__ == "__main__":
    print(main())
