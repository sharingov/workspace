package main

import (
	"os"
)

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

func strRev(s string) string {
	arr := []byte(s)
	for i := 0; i < len(s)/2; i++ {
		j := len(s) - 1 - i
		arr[i], arr[j] = arr[j], arr[i]
	}
	return string(arr)
}

func count(array []byte, b byte) int {
	count := 0
	for _, e := range array {
		if b == e {
			count++
		}
	}
	return count
}

func main() {
	file := os.Stdin
	data := make([]byte, 1e6)
	le, err := file.Read(data)
	if err != nil {
		os.Stdout.WriteString("Not a Raid function\n")
		return
	}
	data = data[:le]
	y := count(data, '\n')
	x := (len(data) - y) / y
	var ans []string
	if string(data) == quadA(x, y) {
		ans = append(ans, "quadA")
	}
	if string(data) == quadB(x, y) {
		ans = append(ans, "quadB")
	}
	if string(data) == quadC(x, y) {
		ans = append(ans, "quadC")
	}
	if string(data) == quadD(x, y) {
		ans = append(ans, "quadD")
	}
	if string(data) == quadE(x, y) {
		ans = append(ans, "quadE")
	}
	if len(ans) == 0 {
		os.Stdout.WriteString("Not a Raid function\n")
		return
	}
	for i, s := range ans {
		if i != 0 {
			os.Stdout.WriteString(" || ")
		}
		os.Stdout.WriteString("[" + s + "]" + " [" + itoa(x) + "]" + " [" + itoa(y) + "]")
	}
	os.Stdout.WriteString("\n")
}

func quad(x, y int, NW, NE, SW, SE, hor, ver rune) string {
	if x <= 0 || y <= 0 {
		return ""
	}
	line := make([]rune, x, x)
	top := make([]rune, x, x)
	bottom := make([]rune, x, x)
	filler := make([]rune, x, x)
	for i := range line {
		line[i] = hor
		filler[i] = ' '
	}
	copy(top, line)
	copy(bottom, line)
	top[x-1] = NE
	bottom[x-1] = SE
	top[0] = NW
	bottom[0] = SW
	filler[0] = ver
	filler[x-1] = ver
	var ans string
	ans += string(top) + "\n"
	for i := 1; i < y; i++ {
		if i == y-1 {
			ans += string(bottom) + "\n"
		} else {
			ans += string(filler) + "\n"
		}
	}
	return ans
}

func quadA(x, y int) string {
	return quad(x, y, 'o', 'o', 'o', 'o', '-', '|')
}

func quadB(x, y int) string {
	return quad(x, y, '/', '\\', '\\', '/', '*', '*')
}

func quadC(x, y int) string {
	return quad(x, y, 'A', 'A', 'C', 'C', 'B', 'B')
}

func quadD(x, y int) string {
	return quad(x, y, 'A', 'C', 'A', 'C', 'B', 'B')
}

func quadE(x, y int) string {
	return quad(x, y, 'A', 'C', 'C', 'A', 'B', 'B')
}
