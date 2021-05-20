package piscine

func LastRune(s string) rune {
	arr := []rune(s)
	return arr[len(arr)-1]
}
