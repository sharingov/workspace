package main

import (
	"os"

	"github.com/01-edu/z01"
)

func strRev(s string) string {
	arr := []byte(s)
	for i := 0; i < len(s)/2; i++ {
		j := len(s) - 1 - i
		arr[i], arr[j] = arr[j], arr[i]
	}
	return string(arr)
}

func convert(s string, b bool) rune {
	s = strRev(s)
	cur := 1
	sum := 0
	for _, val := range s {
		if val < '0' || val > '9' {
			return ' '
		}
		sum += cur * (int(val) - 48)
		cur *= 10
	}
	if sum <= 26 {
		if !b {
			sum += 32
		}
		return rune(sum) + 64
	} else {
		return ' '
	}
}

func main() {
	arr := os.Args[1:]
	upper := false
	if len(arr) > 0 {
		if arr[0] == "--upper" {
			upper = true
			arr = arr[1:]
		}
	} else {
		return
	}
	for _, str := range arr {
		z01.PrintRune(rune(convert(str, upper)))
	}
	z01.PrintRune('\n')
}
