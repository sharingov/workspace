package piscine

func ListSize(l *List) int {
	c := 0
	for p := l.Head; p != nil; c, p = c+1, p.Next {
	}
	return c
}
