package main

func main() {
	const lim = 1000000
	cache := make([]int, lim)
	cache[2] = 2

	longest := 0
	num := 0

	for n := 3; n < lim; n++ {

		chain_len := 0
		var next = n

		for next >= n {
			if next%2 == 1 {
				next = (next*3 + 1) / 2
				chain_len += 2
			} else {
				next /= 2
				chain_len += 1
			}
		}
		chain_len += cache[next]
		cache[n] = chain_len

		if chain_len > longest {
			longest = chain_len
			num = n
		}
	}
	println(num)
}
