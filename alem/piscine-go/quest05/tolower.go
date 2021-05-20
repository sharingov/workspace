package piscine

func ToLower(s string) string {
	arr := []byte(s)
	for i, b := range arr {
		if b >= 65 && b <= 90 {
			arr[i] = b + 32
		}
	}
	return string(arr)
}
