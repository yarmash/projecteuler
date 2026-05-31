package main

import "fmt"

func main() {
	const limit = 100
	sum := limit * (limit + 1) / 2 // arithmetic progression
	squareOfSum := sum * sum
	sumOfSquares := (2*limit + 1) * (limit + 1) * limit / 6 // Sum of the first n squares
	fmt.Println(squareOfSum - sumOfSquares)
}
