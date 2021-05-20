package piscine

func BasicJoin(elems []string) string {
	var ans string
	for _, s := range elems {
		ans += s
	}
	return ans
}
