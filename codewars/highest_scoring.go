package kata

import (
	"strings"
)

func High(s string) string {
	words := strings.Split(s, " ")
	ans, top := "", 0
	for _, word := range words {
		cur := 0
		for _, ch := range word {
			cur += int(ch) - 96
		}
		if cur > top {
			top = cur
			ans = word
		}
	}
	return ans
}
