package piscine

func CountIf(f func(string) bool, tab []string) int {
	counter := 0
	for _, s := range tab {
		if f(s) {
			counter++
		}
	}
	return counter
}
