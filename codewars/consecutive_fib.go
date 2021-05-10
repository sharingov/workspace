package kata

func ProductFib(prod uint64) [3]uint64 {
	var a, b, c uint64 = 0, 1, 0
	for a*b < prod {
		a, b = b, a+b
	}
	if a*b == prod {
		c = 1
	}
	return [3]uint64{a, b, c}
}
