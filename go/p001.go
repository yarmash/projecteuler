package main

import "fmt"

func arithmeticSeries(first int, last int, terms int) int {
	return terms * (first + last) / 2
}

func main() {
	limit := 999
	fmt.Println(arithmeticSeries(3, limit/3*3, limit/3) + arithmeticSeries(5, limit/5*5, limit/5) - arithmeticSeries(15, limit/15*15, limit/15))
}
