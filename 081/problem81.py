#!/usr/bin/python

"""Problem 81: Path sum: two ways"""

from projecteuler import open_data_file

def main():
    f = open_data_file("matrix.txt")
    matrix = [ [int(x) for x in line.split(",")] for line in f ]

    sums = [ [0]*80 for i in range(80) ]
    sums[0][0] = matrix[0][0]

    for i in range(1, 80):
        sums[0][i] = sums[0][i-1] + matrix[0][i]
        sums[i][0] = sums[i-1][0] + matrix[i][0]

    for i in range(1, 80):
        for j in range(1, 80):
            sums[i][j] = matrix[i][j] + min(sums[i-1][j], sums[i][j-1])

    return sums[-1][-1]


if __name__ == "__main__":
    print(main())
