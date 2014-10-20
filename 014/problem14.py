#!/usr/bin/python

"""Problem 14: Longest Collatz sequence"""

def main():

    def get_chain_length(n, cache={2: 2}):
        if not n in cache:
            cache[n] = 2 + get_chain_length((3*n+1)>>1) if n&1 else 1 + get_chain_length(n>>1)
        return cache[n]

    limit = 1000000
    longest = num = 0

    # Look only at the second half of the numbers in the range
    # For every number n ≤ limit//2, 2n is also in the range
    for i in range(limit//2, limit):
        length = get_chain_length(i)

        if length > longest:
            longest = length
            num = i

    return num

if __name__ == "__main__":
    print(main())
