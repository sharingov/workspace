package main

import (
	"os"

	"github.com/01-edu/z01"
)

func printlnStr(s string) {
	for _, ch := range s {
		z01.PrintRune(rune(ch))
	}
	z01.PrintRune('\n')
}

func sort(array []string) {
	for i := 0; i < len(array)-1; i++ {
		min := i
		for j := i + 1; j < len(array); j++ {
			if array[j] < array[min] {
				min = j
			}
		}
		array[i], array[min] = array[min], array[i]
	}
}

func main() {
	arr := os.Args[1:]
	sort(arr)
	for _, str := range arr {
		printlnStr(str)
	}
}
