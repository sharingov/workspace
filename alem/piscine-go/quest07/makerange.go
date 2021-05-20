package piscine

func MakeRange(min, max int) []int {
	n := max - min
	var slice ints
	if n <= 0 {
		return slice
	}
	slice = make(ints, n)
	for i := range slice {
		slice[i] = min + i
	}
	return slice
}
