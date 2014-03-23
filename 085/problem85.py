#!/usr/bin/python

"""Problem 85: Counting rectangles"""


import sys
sys.setrecursionlimit(10000)


def main():
    cache = {}

    def expand(grid, rectangles, next_r, next_c):

        if (next_r, next_c) in cache:
            return cache[(next_r, next_c)]
        elif (next_c, next_r) in cache:
            return cache[(next_c, next_r)]

        if sum(rectangles.values()) >= 2000000:
            return

        if next_r > grid[0]:  # moving down
            # Update counters for existing rectangles.
            for k, v in rectangles.items():
                rectangles[k] += next_c - k[1] + 1

            # Add new rectangles.
            for col in range(1, next_c+1):
                rectangles[next_r, col] = col
        else:  # moving right
            for k, v in rectangles.items():
                rectangles[k] += next_r - k[0] + 1

            for row in range(1, next_r+1):
                rectangles[row, next_c] = row

        grid = [next_r, next_c]
        cache[(next_r, next_c)] = sum(rectangles.values())

        expand(list(grid), rectangles.copy(), next_r, next_c+1)
        expand(list(grid), rectangles.copy(), next_r + 1, next_c)

    rectangles = {(1, 1): 1}
    expand([1, 1], rectangles, 1, 2)

    for k in sorted(cache, key=cache.get, reverse=True):
        if cache[k] < 2000000:
            return k[0]*k[1]


if __name__ == "__main__":
    print(main())
