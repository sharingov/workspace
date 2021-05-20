package piscine

func Join(strs []string, sep string) string {
	var ans string
	for _, s := range strs {
		ans += s + sep
	}
	return ans[:len(ans)-len(sep)]
}
