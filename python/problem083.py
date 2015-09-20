#!/usr/bin/python

"""Problem 83: Path sum: four ways"""

from utils import open_data_file
from heapq import heappush, heappop


def main():
    with open_data_file("matrix.txt") as data_file:
        matrix = [[int(x) for x in line.split(",")] for line in data_file]

    size = 80
    last = size - 1
    distances = [[float("inf")]*size for i in range(size)]
    heap = [(matrix[0][0], 0, 0)]

    # Dijkstra's algorithm, simplified
    while heap:
        distance, row, col = heappop(heap)

        # try to go up, right, down and left, if possible
        for r, c in ((row-1, col), (row, col+1), (row+1, col), (row, col-1)):
            if 0 <= r <= last >= c >= 0:
                new_distance = distance + matrix[r][c]
                if new_distance < distances[r][c]:
                    heappush(heap, (new_distance, r, c))
                    distances[r][c] = new_distance

    return distances[last][last]

if __name__ == "__main__":
    print(main())
