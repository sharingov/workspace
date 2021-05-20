package piscine

func IsUpper(s string) bool {
	for _, r := range s {
		if r < 65 || r > 90 {
			return false
		}
	}
	return true
}
