package main

import (
	"fmt"
	"os"
)

func sort(array []byte) {
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

func help() {
	man := []string{
		"--insert",
		"  -i",
		"	 This flag inserts the string into the string passed as argument.",
		"--order",
		"  -o",
		"	 This flag will behave like a boolean, if it is called it will order the argument.",
	}
	for _, str := range man {
		fmt.Println(str)
	}
}

func main() {
	arr := os.Args[1:]
	if len(arr) == 0 || arr[0] == "--help" || arr[0] == "-h" {
		help()
		return
	}
	var s string
	order := false
	for _, str := range arr {
		if len(str) > 0 && str[0] == '-' {
			if str == "-o" || str == "--order" {
				order = true
			} else {
				if str[1] == '-' {
					s = str[9:] + s
				} else {
					s = str[3:] + s
				}
			}
		} else {
			s = str + s
		}
	}
	if order {
		bytes := []byte(s)
		sort(bytes)
		s = string(bytes)
	}
	fmt.Println(s)
}
