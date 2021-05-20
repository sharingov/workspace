package piscine

func IsAlpha(s string) bool {
	for _, r := range s {
		if !(r >= 48 && r <= 57 || r >= 65 && r <= 90 || r >= 97 && r <= 122) {
			return false
		}
	}
	return true
}
