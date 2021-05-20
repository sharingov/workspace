package piscine

func decToBase(nbr int, base string) string {
	if nbr == 0 {
		return string(base[0])
	}
	n := len(base)
	ans := bytes("")
	for nbr != 0 {
		ans = append(ans, base[nbr%n])
		nbr /= n
	}
	return StrRev(string(ans))
}

func baseToDec(s string, base string) int {
	n := len(base)
	cur := 1
	ans := 0
	for _, r := range StrRev(s) {
		ans += Index(base, string(r)) * cur
		cur *= n
	}
	return ans
}

func ConvertBase(nbr, baseFrom, baseTo string) string {
	return decToBase(baseToDec(nbr, baseFrom), baseTo)
}
