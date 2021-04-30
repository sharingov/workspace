package kata

func ValidBraces(str string) bool {
	a, b, c := 0, 0, 0
	stack := []int{}
	for _, x := range str {
		last_ind := len(stack) - 1
		switch x {
		case '(':
			a++
			stack = append(stack, 1)
		case ')':
			if last_ind < 0 || stack[last_ind] != 1 {
				return false
			}
			a--
			stack = stack[:last_ind]
		case '[':
			b++
			stack = append(stack, 2)
		case ']':
			if last_ind < 0 || stack[last_ind] != 2 {
				return false
			}
			b--
			stack = stack[:last_ind]
		case '{':
			c++
			stack = append(stack, 3)
		case '}':
			if last_ind < 0 || stack[last_ind] != 3 {
				return false
			}
			c--
			stack = stack[:last_ind]
		}
	}
	return a == 0 && b == 0 && c == 0
}
