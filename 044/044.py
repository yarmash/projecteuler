from math import sqrt


def is_pentagonal(n):
	k = (sqrt(24*n+1)+1)/6
	return k == int(k)

def nth_p(n): # calculate the nth pentagonal number
	return n*(3*n - 1)/2


def min_difference():
    diffs = []

    mindiff, diff, n = 0, 1, 1

    while mindiff < diff:
        n += 1
        diff += 3 # the difference increases by 3

        diffs.append(0)

        for i in range(len(diffs)):
            diffs[i] += diff

            if n != (i+1) and is_pentagonal(diffs[i]):
                if is_pentagonal(nth_p(i+1) + nth_p(n)):
                    mindiff = min(mindiff, diffs[i]) if mindiff else diffs[i]
    return mindiff

print min_difference()
