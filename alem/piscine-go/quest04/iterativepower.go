package piscine

func IterativePower(nb int, power int) int {
	if power < 0 {
		return 0
	}
	ans := 1
	for i := 0; i < power; i++ {
		ans *= nb
	}
	return ans
}
