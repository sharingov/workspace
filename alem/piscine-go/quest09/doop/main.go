package main

import (
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

	s = strRev(string(arr))
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

func operate(a, b int, op byte) int {
	switch op {
	case '+':
		c := a + b
		if a > 0 && b > 0 && c <= 0 {
			panic("Overflow")
		} else if a < 0 && b < 0 && c >= 0 {
			panic("Overflow")
		}
		return c
	case '-':
		if b == -9223372036854775808 {
			if a >= 0 {
				panic("Overflow")
			} else {
				return 9223372036854775807 - (a - 1)
			}
		} else {
			return operate(a, -b, '+')
		}
	case '/':
		if b == 0 {
			os.Stdout.WriteString("No division by 0\n")
		}
		return a / b
	case '*':
		c := 0
		coeff := 1
		if b < 0 {
			if b == -9223372036854775808 {
				if a == 1 {
					return b
				} else if a == 0 {
					return 0
				} else {
					panic("Overflow")
				}
			}
			coeff = -1
			b = -b
		}
		for i := 0; i < b; i++ {
			c = operate(c, a, '+')
		}
		return c * coeff
	case '%':
		if b == 0 {
			os.Stdout.WriteString("No modulo by 0\n")
		}
		return a % b
	default:
		panic("Invalid operator")
	}
}

func main() {
	args := os.Args[1:]
	defer func() {
		if err := recover(); err != nil {
			return
		}
	}()
	val := operate(atoi(args[0]), atoi(args[2]), args[1][0])
	os.Stdout.WriteString(itoa(val) + "\n")
}
