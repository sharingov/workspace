package main

import (
	"fmt"
	"os"
)

func any(f func(string) bool, a []string) bool {
	for _, s := range a {
		if f(s) {
			return true
		}
	}
	return false
}

func alert(s string) bool {
	return s == "01" || s == "galaxy" || s == "galaxy 01"
}

func main() {
	if any(alert, os.Args[1:]) {
		fmt.Println("Alert!!!")
	}
}
