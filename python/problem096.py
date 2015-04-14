#!/usr/bin/python

"""Problem 96: Su Doku"""

from utils import open_data_file
import copy
from itertools import combinations, product
from collections import defaultdict

numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}


def get_candidates(grid):
    candidates = [[set() for j in range(9)] for i in range(9)]

    for min_row in range(0, 9, 3):
        for min_col in range(0, 9, 3):
            crosshatch_square(grid, min_row, min_col, pencilin=True, candidates=candidates)

    tmp = copy.deepcopy(candidates)

    while True:
        # number claiming

        # When a candidate number only appears in one row or column of a box, the box 'claims' that number within the entire row or column.
        # When two squares in the same area (row, column or box) have identical two-number candidate lists, you can remove both numbers from other candidate lists in that area.

        for min_row in range(0, 9, 3):
            for min_col in range(0, 9, 3):

                for row in range(min_row, min_row+3):
                    for col in range(min_col, min_col+3):

                        # claim row
                        for c in candidates[row][col]:
                            if all(c not in candidates[r][coll] for r in list(range(min_row, row)) + list(range(row+1, min_row+3)) for coll in range(min_col, min_col+3)):

                                for colll in list(range(min_col)) + list(range(min_col+3, 9)):
                                    candidates[row][colll] -= {c}

                        # claim column
                        for c in candidates[row][col]:
                            if all(c not in r[coll] for r in candidates[min_row:min_row+3] for coll in [x for x in range(min_col, min_col+3) if x != col]):

                                for r in list(range(min_row)) + list(range(min_row+3, 9)):
                                    candidates[r][col] -= {c}

        for i in range(2, 5):
            for row in range(9):

                for cols in combinations(range(9), i):
                    s = set()

                    if all(1 <= len(candidates[row][c]) <= i for c in cols):
                        for c in cols:
                            s |= candidates[row][c]

                    if len(s) == i:

                        for c in range(9):
                            if c not in cols:
                                candidates[row][c] -= s

            for col in range(9):

                for rows in combinations(range(9), i):
                    s = set()

                    if all(1 <= len(candidates[row][col]) <= i for row in rows):
                        for row in rows:
                            s |= candidates[row][col]

                    if len(s) == i:
                        for r in range(9):
                            if r not in rows:
                                candidates[r][col] -= s

            for min_row in range(0, 9, 3):
                for min_col in range(0, 9, 3):

                    for points in combinations(product(range(min_row, min_row+3), range(min_col, min_col+3)), i):
                        s = set()

                        if all(1 <= len(candidates[r][c]) <= i for r, c in points):
                            for r, c in points:
                                s |= candidates[r][c]

                        if len(s) == i:
                            for r in range(min_row, min_row+3):
                                for c in range(min_col, min_col+3):
                                    if not (r, c) in points:
                                        candidates[r][c] -= s

        # excluded candidates
        #Within an area (row, column or box), when a set of N candidate lists contain all occurrences of a set of N candidate numbers, other numbers can be removed from those lists
        for i in range(3, 5):
            for row in range(9):

                for cols in combinations(range(9), i):
                    s = set()

                    for c in cols:
                        s &= candidates[row][c]

                    if len(s) == i:
                        for c in cols:
                            candidates[row][c] = set(s)

            for col in range(9):
                for rows in combinations(range(9), i):
                    s = set()

                    for row in rows:
                        s &= candidates[row][col]

                    if len(s) == i:
                        for r in rows:
                            candidates[r][col] = set(s)

            for min_row in range(0, 9, 3):
                for min_col in range(0, 9, 3):

                    for points in combinations(product(range(min_row, min_row+3), range(min_col, min_col+3)), i):
                        s = set()
                        for r, c in points:
                            s &= candidates[r][c]

                    if len(s) == i:
                        for r, c in points:
                            candidates[r][c] = set(s)

        # box line reduction
        # If all occurrences of a candidate within a row or column fall inside the same box, then other occurrences of that candidate can be removed from that box

        for min_row in range(0, 9, 3):
            for row in range(min_row, min_row+3):

                for c in numbers:
                    indexes = []

                    for col in range(9):
                        if c in candidates[row][col]:
                            indexes.append(col)

                    if indexes:
                        # 1st box
                        if all(0 <= i <= 2 for i in indexes):
                            for r in range(min_row, min_row+3):
                                if r == row: continue
                                for coll in range(3):
                                    candidates[r][coll] -= {c}

                        if all(3 <= i <= 5 for i in indexes):
                            for r in range(min_row, min_row+3):
                                if r == row: continue
                                for coll in range(3, 6):
                                    candidates[r][coll] -= {c}

                        if all(6 <= i <= 8 for i in indexes):
                            for r in range(min_row, min_row+3):
                                if r == row: continue
                                for coll in range(6, 9):
                                    candidates[r][coll] -= {c}

        for min_col in range(0, 9, 3):
            for col in range(min_col, min_col+3):
                for c in numbers:
                    indexes = []

                    for row in range(9):
                        if c in candidates[row][col]:
                            indexes.append(row)

                    if indexes:
                        if all(0 <= i <= 2 for i in indexes):
                            for r in range(3):
                                for coll in range(min_col, min_col+3):
                                    if coll == col: continue
                                    candidates[r][coll] -= {c}

                        if all(3 <= i <= 5 for i in indexes):
                            for r in range(3, 6):
                                for coll in range(min_col, min_col+3):
                                    if coll == col: continue
                                    candidates[r][coll] -= {c}

                        if all(6 <= i <= 8 for i in indexes):
                            for r in range(6, 9):
                                for coll in range(min_col, min_col+3):
                                    if coll == col: continue
                                    candidates[r][coll] -= {c}

        # When there are

        #   only two possible cells for a value in each of two different rows,
        #   and these candidates lie also in the same columns,
        #     then all other candidates for this value in the columns can be eliminated.

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
                    for coll in k:
                        candidates[r][coll] -= {num}

        if candidates == tmp:
            break
        tmp = copy.deepcopy(candidates)

    return candidates


def pencil_in(grid):

    filled = 0
    candidates = get_candidates(grid)

    # check candidates

    for row in range(9):
        for col in range(9):
            # Single-candidate squares
            if len(candidates[row][col]) == 1:
                grid[row][col] = candidates[row][col].pop()
                filled += 1

    while sum([crosshatch_square(grid, min_row, min_col) for min_row in range(0, 9, 3) for min_col in range(0, 9, 3)]):
        pass

    candidates = get_candidates(grid)

    # check candidates
    for row in range(9):
        for col in range(9):

            # single-square candidates (rows)
            single = None
            for c in candidates[row][col]:
                if all(c not in cc for cc in candidates[row][:col] + candidates[row][col+1:]):
                    single = grid[row][col] = c
                    filled += 1
                    break
            if single:
                candidates[row][col].remove(single)


    while sum([crosshatch_square(grid, min_row, min_col) for min_row in range(0, 9, 3) for min_col in range(0, 9, 3)]):
        pass

    candidates = get_candidates(grid)

    # check candidates
    for row in range(9):
        for col in range(9):
            # single-square candidates (column)
            single = None
            for c in candidates[row][col]:
                if all(c not in cc for cc in [r[col] for r in candidates[:row]] + [r[col] for r in candidates[row+1:]]):
                    single = grid[row][col] = c
                    filled += 1
                    break

            if single:
                candidates[row][col].remove(single)

    while sum([crosshatch_square(grid, min_row, min_col) for min_row in range(0, 9, 3) for min_col in range(0, 9, 3)]):
        pass

    candidates = get_candidates(grid)

    # check candidates
    for min_row in range(0, 9, 3):
        for min_col in range(0, 9, 3):

            for row in range(min_row, min_row+3):
                for col in range(min_col, min_col+3):

                    # single-square candidates (box)
                    single = None
                    for c in candidates[row][col]:
                        if all(c not in cc for cc in candidates[min_row][min_col:min_col+3] + candidates[min_row+1][min_col:min_col+3] + candidates[min_row+2][min_col:min_col+3]):
                            single = grid[row][col] = c
                            filled += 1
                            break

                    if single:
                        candidates[row][col].remove(single)

    while sum([crosshatch_square(grid, min_row, min_col) for min_row in range(0, 9, 3) for min_col in range(0, 9, 3)]):
        pass
    return filled


def crosshatch_square(grid, min_row, min_col, pencilin=False, candidates=None):
    max_row = min_row + 3
    max_col = min_col + 3
    used_numbers = {grid[row][col] for row in range(min_row, max_row)
                    for col in range(min_col, max_col)}
    unused_numbers = numbers - used_numbers

    # "0" - empty, "X" - crosshatched

    filled = 0

    for num in unused_numbers:
        for row in range(min_row, max_row):
            if num in grid[row][:min_col] + grid[row][max_col:]:
                for col in range(min_col, max_col):
                    if grid[row][col] == "0":
                        grid[row][col] = "X"

        for col in range(min_col, max_col):
            if num in [row[col] for row in grid[:min_row] + grid[max_row:]]:
                for row in range(min_row, max_row):
                    if grid[row][col] == "0":
                        grid[row][col] = "X"

        cnt = 0
        for row in range(min_row, max_row):
            for col in range(min_col, max_col):
                if grid[row][col] == "0":
                    cnt += 1

        if cnt == 1:
            for row in range(min_row, max_row):
                for col in range(min_col, max_col):
                    if grid[row][col] == "0":
                        grid[row][col] = num
                        filled = 1
        elif pencilin:
            for row in range(min_row, max_row):
                for col in range(min_col, max_col):
                    if grid[row][col] == "0":
                        candidates[row][col].add(num)
        # cleanup
        for row in range(min_row, max_row):
            for col in range(min_col, max_col):
                if grid[row][col] == "X":
                    grid[row][col] = "0"

    return filled


def solve_puzzle(grid):
    """Solve a sudoku puzzle"""

    # try crosshatching

    while sum([crosshatch_square(grid, min_row, min_col) for min_row in range(0, 9, 3) for min_col in range(0, 9, 3)]):
        pass

    if all("0" not in line for line in grid):
        return grid

    while pencil_in(grid):
        pass

    return grid


def verify_grid(grid):
    for row in grid:
        assert set(row) == numbers

    for col in range(9):
        assert set([row[col] for row in grid]) == numbers

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            assert set(grid[row][col:col+3] + grid[row+1][col:col+3] + grid[row+2][col:col+3]) == numbers


def main():
    s = 0

    with open_data_file("sudoku.txt") as data_file:
        grid = []

        for i, line in enumerate(data_file):
            if i % 10 == 0:
                continue
            grid.append([x for x in line.rstrip()])

            if len(grid) == 9:
                solve_puzzle(grid)
                assert("0" not in line for line in grid)
                s += int(grid[0][0]+grid[0][1]+grid[0][2])
                grid = []
    return s

if __name__ == "__main__":
    print(main())
