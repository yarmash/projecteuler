package main

import "fmt"

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int) int {
	return a / gcd(a, b) * b
}

func main() {
	const limit = 20

	result := 1
	for i := 1; i <= limit; i++ {
		result = lcm(result, i)
	}

	fmt.Println(result)
}
