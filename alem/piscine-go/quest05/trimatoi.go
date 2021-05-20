package piscine

func TrimAtoi(s string) int {
	arr := bytes(s)
	coeff := 1

	if len(arr) == 0 {
		return 0
	}

	for i, b := range arr {
		if b >= 48 && b <= 57 || b == 43 {
			arr = arr[i:]
			break
		} else if b == 45 {
			coeff = -1
			arr = arr[i:]
			break
		}
	}

	s = StrRev(string(arr))
	cur := 1
	sum := 0
	for _, val := range s {
		if val < 48 || val > 57 {
			continue
		}
		sum += cur * (int(val) - 48)
		cur *= 10
	}

	return sum * coeff
}
