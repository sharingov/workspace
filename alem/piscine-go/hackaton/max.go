package piscine

func Max(a []int) int {
	if len(a) == 0 {
		return 0
	}
	max := a[1]
	for _, e := range a[1:] {
		if e > max {
			max = e
		}
	}
	return max
}
