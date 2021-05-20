package piscine

func BasicAtoi2(s string) int {
	arr := []byte(s)
	i := 0
	if StrLen(s) == 0 {
		return 0
	}
	for ; arr[i] == 0; i++ {
	}
	s = StrRev(string(arr[i:]))
	cur := 1
	sum := 0
	for _, val := range s {
		if val < 48 || val > 57 {
			return 0
		}
		sum += cur * (int(val) - 48)
		cur *= 10
	}
	return sum
}
