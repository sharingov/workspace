package piscine

func IterativeFactorial(nb int) int {
	if nb < 0 || nb > 20 {
		return 0
	}
	ans := 1
	for i := 1; i <= nb; i++ {
		ans *= i
	}
	return ans
}
