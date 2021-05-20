package piscine

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
