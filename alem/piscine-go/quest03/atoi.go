package piscine

func Atoi(s string) int {
	arr := []byte(s)
	i := 0
	coeff := 1

	if StrLen(s) == 0 {
		return 0
	}

	if arr[0] == '-' {
		arr = arr[1:]
		coeff = -1
	} else if arr[0] == '+' {
		arr = arr[1:]
	}

	if StrLen(string(arr)) == 0 {
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

	return sum * coeff
}
