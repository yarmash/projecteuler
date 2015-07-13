package main

import "fmt"

var cache = map[int]int{2: 2}

func get_chain_len(n int) int {

	if cache[n] == 0 {
		if n%2 == 0 {
			cache[n] = 1 + get_chain_len(n/2)
		} else {
			cache[n] = 2 + get_chain_len((3*n+1)/2)
		}
	}
	return cache[n]
}

func main() {
	const lim = 1000000
	longest := 0
	num := 0

	for i := lim / 2; i < lim; i++ {
		length := get_chain_len(i)
		if length > longest {
			longest = length
			num = i
		}
	}
	fmt.Printf("%d\n", num)
}
