package piscine

func Capitalize(s string) string {
	arr := bytes(s)
	first := true
	for i, b := range arr {
		if b >= 48 && b <= 57 || b >= 65 && b <= 90 || b >= 97 && b <= 122 {
			if first && b >= 97 && b <= 122 {
				arr[i] -= 32
			} else if !first && b >= 65 && b <= 90 {
				arr[i] += 32
			}
			first = false
		} else {
			first = true
		}
	}
	return string(arr)
}
