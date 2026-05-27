package main

import (
	"fmt"
	"math"
)

func main() {
	var num int64 = 600851475143
	maxFactor := int64(math.Sqrt(float64(num)))
	var factor int64 = 3
	var lastFactor int64 = 3

	for num > 1 && factor <= maxFactor {
		if num%factor == 0 {
			lastFactor = factor
			for num%factor == 0 {
				num /= factor
			}
			maxFactor = int64(math.Sqrt(float64(num)))
		}
		factor += 2
	}
	if num == 1 {
		fmt.Println(lastFactor)
	} else {
		fmt.Println(num)
	}
}
