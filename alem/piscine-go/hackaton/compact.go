package piscine

func Compact(ptr *[]string) int {
	count := 0
	elements := make(map[int]string)
	for _, s := range *ptr {
		if s != "" {
			elements[count] = s
			count++
		}
	}
	arr := make([]string, count)
	for i, e := range elements {
		arr[i] = e
	}
	*ptr = arr
	return count
}
