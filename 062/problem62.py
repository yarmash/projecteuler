#!/usr/bin/python2

def main(N=5):
    num, bound = 1, 10
    cubes = {}
    candidates = []

    while True:
        cube = num**3
        key = "".join(sorted(str(cube)))

        if cube > bound: # safe to return a candidate
            if candidates and filter(lambda k: len(cubes[k]) == N, candidates):
                return min(map(min, map(lambda k: cubes[k], candidates)))
            bound *= 10

        if key in cubes:
            cubes[key].append(cube)

            if len(cubes[key]) == N:
                candidates.append(key)
        else:
            cubes[key] = [cube]
        num += 1


if __name__ == "__main__":
    print main()
