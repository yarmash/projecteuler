#!/usr/bin/python2

"""Magic 5-gon ring"""

from operator import itemgetter

def main():
    numbers = set(xrange(1, 11))
    sides = [0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1]
    rotations = map(lambda i: itemgetter(*sides[i:] + sides[:i]), xrange(0, len(sides), 3))
    solutions = []

    def search(ring):
        node = len(ring) - 1

        # check sums
        if node == 4 and ring[0] + ring[1] != ring[3] + ring[4] \
            or node == 6 and ring[2] + ring[3] != ring[5] + ring[6] \
            or node == 8 and ring[4] + ring[5] != ring[7] + ring[8] \
            or node == 9 and ring[6] + ring[7] != ring[1] + ring[9]:
            return

        candidates = numbers - set(ring)

        if candidates:
            for c in candidates:
                search(ring + [c])
        else:
            solutions.append(min(map(lambda rotation: rotation(ring), rotations)))

    # 10 must be an outer node since the answer is 16-digit
    search([10])

    return "".join(map(str, max(solutions)))


if __name__ == "__main__":
    print main()
