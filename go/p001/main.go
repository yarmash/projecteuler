package main

import "fmt"

func sumMultiplesUpTo(limit, divisor int) int {
	n := limit / divisor
	return divisor * n * (n + 1) / 2
}

func main() {
	const limit = 999

	fmt.Println(
		sumMultiplesUpTo(limit, 3) +
			sumMultiplesUpTo(limit, 5) -
			sumMultiplesUpTo(limit, 15),
	)
}
