package piscine

func ActiveBits(n int) int {
	count := 0
	for ; n != 0; n /= 2 {
		count += n % 2
	}
	return count
}
