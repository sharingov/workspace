package piscine

func Index(s, substr string) int {
	for i := 0; i < len(s)-len(substr)+1; i++ {
		if Compare(s[i:i+len(substr)], substr) == 0 {
			return i
		}
	}
	return -1
}
