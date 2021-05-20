package piscine

func CollatzCountdown(n int) int {
	if n <= 0 {
		return -1
	}
	count := 0
	for n != 1 {
		if n%2 == 0 {
			n /= 2
		} else {
			n = 3*n + 1
		}
		count++
	}
	return count
}
