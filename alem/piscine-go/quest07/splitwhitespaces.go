package piscine

func SplitWhiteSpaces(s string) []string {
	var slice strings
	i, j := 0, 0
	for ; j < len(s); j++ {
		if s[j] == ' ' || s[j] == '\t' || s[j] == '\n' {
			if j > i {
				slice = append(slice, s[i:j])
			}
			i = j + 1
		}
	}
	if j > i {
		slice = append(slice, s[i:j])
	}
	return slice
}
