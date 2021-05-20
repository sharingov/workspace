package piscine

func Unmatch(a []int) int {
	le := len(a)
	for i := 0; i < le; i++ {
		count := 0
		for j := 0; j < le; j++ {
			if a[i] == a[j] {
				count++
			}
		}
		if count%2 == 1 {
			return a[i]
		}
	}
	return -1
}
