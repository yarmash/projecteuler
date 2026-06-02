package utils

func PrimeSieveLazy() func() int {
	composites := make(map[int][]int)
	n := 2

	return func() int {
		if n == 2 {
			n = 3
			return 2
		}

		for {
			factors, ok := composites[n]
			if !ok {
				prime := n
				// Smaller multiples already have a smaller prime factor, so start at p*p.
				composites[prime*prime] = []int{prime}
				n += 2
				return prime
			}

			delete(composites, n)

			for _, prime := range factors {
				next := n + 2*prime
				composites[next] = append(composites[next], prime)
			}

			n += 2
		}
	}
}
