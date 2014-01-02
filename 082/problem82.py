#!/usr/bin/python

"""Problem 82: Path sum: three ways"""

from projecteuler import open_data_file

def main():
    f = open_data_file("matrix.txt")
    matrix = [ [int(x) for x in line.split(",")] for line in f ]

    size = len(matrix)
    best = [row[0] for row in matrix] # first column

    for col in range(1, size):
        column = [ matrix[row][col] + best[row] for row in range(size) ]

        for row in range(1, size):
            if column[row-1] + matrix[row][col] < column[row]:
                column[row] = column[row-1] + matrix[row][col]

        for row in range(size-2, -1, -1):
            if column[row+1] + matrix[row][col] < column[row]:
                column[row] = column[row+1] + matrix[row][col]
        best = column

    return min(best)


if __name__ == "__main__":
    print(main())
