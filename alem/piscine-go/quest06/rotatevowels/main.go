package main

import (
	"os"

	"github.com/01-edu/z01"
)

type enum struct {
	index int
	b     byte
}

func printlnStr(s string) {
	for _, ch := range s {
		z01.PrintRune(rune(ch))
	}
	z01.PrintRune('\n')
}

func join(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	var ans string
	for _, s := range strs {
		ans += s + " "
	}
	return ans
}

func index(s, substr string) int {
	for i := 0; i < len(s)-len(substr)+1; i++ {
		if s[i:i+len(substr)] == substr {
			return i
		}
	}
	return -1
}

func main() {
	s := join(os.Args[1:])
	vowels := "aeiouAEIOU"
	var arr []enum
	for i, b := range s {
		if index(vowels, string(b)) > -1 {
			arr = append(arr, enum{index: i, b: byte(b)})
		}
	}
	bytes := []byte(s)
	for i := 0; i < len(arr)/2; i++ {
		j := len(arr) - 1 - i
		x, y := arr[i], arr[j]
		bytes[x.index] = y.b
		bytes[y.index] = x.b
	}
	printlnStr(string(bytes))
}
