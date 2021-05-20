package piscine

func NRune(s string, n int) rune {
	arr := []rune(s)
	ans := rune(0)
	defer func() {
		recover()
	}()
	ans = arr[n-1]
	return ans
}
