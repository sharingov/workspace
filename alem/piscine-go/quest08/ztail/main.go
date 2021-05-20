package main

import (
	"fmt"
	"os"
)

func strRev(s string) string {
	arr := []byte(s)
	for i := 0; i < len(s)/2; i++ {
		j := len(s) - 1 - i
		arr[i], arr[j] = arr[j], arr[i]
	}
	return string(arr)
}

func atoi(s string) int {
	if len(s) == 0 {
		return 0
	}
	arr := []byte(s)
	coeff := 1
	if arr[0] == '-' {
		arr = arr[1:]
		coeff = -1
	} else if arr[0] == '+' {
		arr = arr[1:]
	}

	if len(arr) == 0 {
		return 0
	}

	s = strRev(string(arr))
	cur := 1
	sum := 0
	for _, val := range s {
		if val < '0' || val > '9' {
			return 0
		}
		sum += cur * (int(val) - 48)
		cur *= 10
	}

	return sum * coeff
}

func main() {
	n := atoi(os.Args[2])
	args := os.Args[3:]
	several := false
	if len(args) > 1 {
		several = true
	}
	for i, s := range args {
		arr, err := os.ReadFile(s)
		if err != nil {
			fmt.Printf("%s\n", err.Error())
			continue
		}
		if several {
			if i != 0 {
				fmt.Printf("\n")
			}
			fmt.Printf("==> %s <==\n", s)
		}
		fmt.Printf("%s", arr[len(arr)-n:])
	}
}
