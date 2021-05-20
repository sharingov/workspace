package piscine

func StrRev(s string) string {
	arr := []byte(s)
	for i := 0; i < StrLen(s)/2; i++ {
		arr[i], arr[StrLen(s)-1-i] = arr[StrLen(s)-1-i], arr[i]
	}
	return string(arr)
}
