package piscine

func AdvancedSortWordArr(a []string, f func(a, b string) int) {
	s := strings(a)
	s.Sort()
	a = s
}
