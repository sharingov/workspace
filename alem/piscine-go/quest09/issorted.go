package piscine

func IsSorted(f func(a, b int) int, a []int) bool {
	descend := 0
	for i := range a {
		if i == 0 {
			continue
		}
		n := f(a[i-1], a[i])
		if n != 0 {
			n = n / Abs(n)
		}
		if descend == 0 {
			descend = n
		} else if n == -descend {
			return false
		}
	}
	return true
}
