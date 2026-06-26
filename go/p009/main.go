package main

import "fmt"

func main() {
	const sum = 1000

	for a := 1; a < sum/3; a++ {
		// From a+b+c=sum and a^2+b^2=c^2, solve for b in terms of a
		numerator := sum*sum - 2*sum*a
		denominator := 2 * (sum - a)

		if numerator%denominator != 0 {
			continue
		}

		b := numerator / denominator
		c := sum - a - b

		fmt.Println(a * b * c)
		return
	}
}
