package main

import "github.com/01-edu/z01"

type point struct{ x, y int }

func strRev(s string) string {
	arr := []byte(s)
	for i := 0; i < len(s)/2; i++ {
		j := len(s) - 1 - i
		arr[i], arr[j] = arr[j], arr[i]
	}
	return string(arr)
}

func itoa(n int) string {
	if n == 0 {
		return "0"
	}
	arr := []byte("")
	neg := false
	if n < 0 {
		neg = true
		n = -n
	}
	for n != 0 {
		temp := n % 10
		arr = append(arr, byte(temp)+48)
		n = n / 10
	}
	if neg {
		arr = append(arr, '-')
	}
	return strRev(string(arr))
}

func printStr(s string) {
	for _, r := range s {
		z01.PrintRune(r)
	}
}

func setPoint(ptr *point) {
	ptr.x = 42
	ptr.y = 21
}

func main() {
	points := &point{}
	setPoint(points)
	s := "x = " + itoa(points.x) + ", y = " + itoa(points.y) + "\n"
	printStr(s)
}
