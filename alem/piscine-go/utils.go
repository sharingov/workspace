package piscine

import "github.com/01-edu/z01"

type (
	ints    []int
	bytes   []byte
	strings []string
)

type NodeL struct {
	Data interface{}
	Next *NodeL
}

type List struct {
	Head *NodeL
	Tail *NodeL
}

type TreeNode struct {
	Left, Right, Parent *TreeNode
	Data                string
}

func PrintStr(s string) {
	for _, r := range s {
		z01.PrintRune(r)
	}
}

func PrintlnStr(s string) {
	for _, r := range s {
		z01.PrintRune(r)
	}
	z01.PrintRune('\n')
}

func PrintlnSlice(slice []int) {
	for _, i := range slice {
		z01.PrintRune(rune(i) + 48)
	}
	z01.PrintRune('\n')
}

func Atoi(s string) int {
	if s == "-9223372036854775808" {
		return -9223372036854775808
	}
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

	s = StrRev(string(arr))
	cur := 1
	sum := 0
	for _, val := range s {
		if val < '0' || val > '9' {
			panic("Invalid input")
		}
		sum += cur * (int(val) - 48)
		if cur != 1 && cur%10 != 0 || sum < 0 {
			panic("Overflow")
		}
		cur *= 10
	}

	return sum * coeff
}

func Itoa(n int) string {
	if n == 0 {
		return "0"
	}
	arr := bytes("")
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
	return StrRev(string(arr))
}

func StrRev(s string) string {
	arr := bytes(s)
	for i := 0; i < len(s)/2; i++ {
		j := len(s) - 1 - i
		arr[i], arr[j] = arr[j], arr[i]
	}
	return string(arr)
}

func (array ints) Sort() {
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

func (array bytes) Sort() {
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

func (array strings) Sort() {
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

func Index(s, substr string) int {
	a := len(s)
	b := len(substr)
	for i := 0; i <= a-b; i++ {
		if s[i:i+b] == substr {
			return i
		}
	}
	return -1
}

func Join(strs []string, sep string) string {
	var ans string
	for _, s := range strs {
		ans += s + sep
	}
	return ans[:len(ans)-len(sep)]
}

func Split(s, sep string) []string {
	var slice strings
	for i := Index(s, sep); ; i = Index(s, sep) {
		if i == -1 {
			slice = append(slice, s)
			break
		}
		slice = append(slice, s[:i])
		s = s[i+len(sep):]
	}
	return slice
}

func Abs(n int) int {
	if n < 0 {
		n = -n
	}
	return n
}

func Any(f func(string) bool, a []string) bool {
	for _, s := range a {
		if f(s) {
			return true
		}
	}
	return false
}

func (array ints) Count(n int) int {
	count := 0
	for _, e := range array {
		if n == e {
			count++
		}
	}
	return count
}

func (array bytes) Count(b byte) int {
	count := 0
	for _, e := range array {
		if b == e {
			count++
		}
	}
	return count
}

func (array strings) Count(s string) int {
	count := 0
	for _, e := range array {
		if s == e {
			count++
		}
	}
	return count
}

func Min(a, b int) int {
	if a <= b {
		return a
	} else {
		return b
	}
}

func Max(a, b int) int {
	if a >= b {
		return a
	} else {
		return b
	}
}
