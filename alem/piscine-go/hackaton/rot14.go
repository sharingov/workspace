package piscine

func Rot14(s string) string {
	arr := bytes(s)
	for i, b := range arr {
		if b >= 'A' && b <= 'Z' {
			arr[i] = (b-65+14)%26 + 65
		} else if b >= 'a' && b <= 'z' {
			arr[i] = (b-97+14)%26 + 97
		}
	}
	return string(arr)
}
