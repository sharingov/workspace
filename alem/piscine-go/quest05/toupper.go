package piscine

func ToUpper(s string) string {
	arr := []byte(s)
	for i, b := range arr {
		if b >= 97 && b <= 122 {
			arr[i] = b - 32
		}
	}
	return string(arr)
}
