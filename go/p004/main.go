package main

import "fmt"

func isPalindrome(number, base int) bool {
	forward := number
	reverse := 0
	for number > 0 {
		reverse = reverse*base + number%base
		number /= base
	}
	return forward == reverse
}

func main() {
	const min = 100
	const max = 999

	largest := 0

	for x := max; x >= min; x-- {
		for y := x; y >= min; y-- {
			product := x * y
			if product <= largest {
				break
			}
			if isPalindrome(product, 10) {
				largest = product
			}
		}
	}
	fmt.Println(largest)
}
