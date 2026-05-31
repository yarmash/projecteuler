package main

import "fmt"

func main() {
	const limit = 4_000_000

	prevEven, currEven, sum := 0, 2, 0

	for currEven <= limit {
		sum += currEven
		prevEven, currEven = currEven, 4*currEven+prevEven
	}

	fmt.Println(sum)
}
