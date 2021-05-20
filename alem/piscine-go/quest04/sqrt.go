package piscine

func Sqrt(nb int) int {
	for i := 0; ; i++ {
		if i*i == nb {
			return i
		} else if i*i > nb {
			return 0
		}
	}
}
