package piscine

func IsLower(s string) bool {
	for _, r := range s {
		if r < 97 || r > 122 {
			return false
		}
	}
	return true
}
