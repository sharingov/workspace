package piscine

func floorSqrt(nb int) int {
	for i := 0; ; i++ {
		if i*i == nb {
			return i
		} else if i*i > nb {
			return i - 1
		}
	}
}

func IsPrime(nb int) bool {
	if nb < 2 {
		return false
	}
	for i := 2; i <= floorSqrt(nb); i++ {
		if nb%i == 0 {
			return false
		}
	}
	return true
}
