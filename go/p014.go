package main

import "fmt"

func main() {
	const limit = 1_000_000

	cache := make([]int, limit)
	cache[2] = 2 // Sequence length including the starting value

	longest := 0
	num := 0

	for n := 3; n < limit; n++ {
		chainLen := 0
		next := n

		for next >= n {
			if next%2 == 1 {
				// For odd n: n -> 3n+1 -> (3n+1)/2
				next = (next*3 + 1) / 2
				chainLen += 2
			} else {
				next /= 2
				chainLen++
			}
		}
		chainLen += cache[next]
		cache[n] = chainLen

		if chainLen > longest {
			longest = chainLen
			num = n
		}
	}

	fmt.Println(num)
}
