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

func main() {
	for _, str := range os.Args[1:] {
		printlnStr(str)
	}
}
