package piscine

func PrintNbrBase(nbr int, base string) {
	set := make(map[byte]bool)
	for _, b := range base {
		if set[byte(b)] {
			PrintStr("NV")
			return
		} else {
			set[byte(b)] = true
		}
	}
	if Index(base, "-") != -1 || Index(base, "+") != -1 || len(base) < 2 {
		PrintStr("NV")
		return
	}
	n := len(base)
	coeff := 1
	ans := bytes("")
	if nbr < 0 {
		coeff = -1
	} else if nbr == 0 {
		PrintStr("0")
		return
	}
	for nbr != 0 {
		ans = append(ans, base[(nbr%n)*coeff])
		nbr /= n
	}
	if coeff == -1 {
		ans = append(ans, '-')
	}
	PrintStr(StrRev(string(ans)))
}
