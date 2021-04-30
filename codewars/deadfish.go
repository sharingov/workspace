package kata

func Parse(data string) []int {
	i := 0
	arr := []int{}
	for _, ch := range data {
		switch ch {
		case 'i':
			i++
		case 'd':
			i--
		case 's':
			i *= i
		case 'o':
			arr = append(arr, i)
		}
	}
	return arr
}
