package main

import (
	"fmt"
	"projecteuler/utils"
)

func main() {
	const target = 10001

	sieve := utils.PrimeSieveLazy()
	prime := 0
	for i := 0; i < target; i++ {
		prime = sieve()
	}

	fmt.Println(prime)
}
