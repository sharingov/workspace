package piscine

func AtoiBase(s string, base string) int {
	set := make(map[byte]bool)
	for _, b := range base {
		if set[byte(b)] {
			return 0
		} else {
			set[byte(b)] = true
		}
	}
	if Index(base, "-") != -1 || Index(base, "+") != -1 || len(base) < 2 {
		return 0
	}
	n := len(base)
	cur := 1
	ans := 0
	for _, r := range StrRev(s) {
		ans += Index(base, string(r)) * cur
		cur *= n
	}
	return ans
}
