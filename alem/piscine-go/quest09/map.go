package piscine

func Map(f func(int) bool, a []int) []bool {
	var arr []bool
	for _, e := range a {
		arr = append(arr, f(e))
	}
	return arr
}
