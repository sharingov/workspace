package piscine

func IsNumeric(s string) bool {
	for _, r := range s {
		if r < 48 || r > 57 {
			return false
		}
	}
	return true
}
