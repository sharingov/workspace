package piscine

func CompStr(a, b interface{}) bool {
	return a == b
}

func ListFind(l *List, ref interface{}, comp func(a, b interface{}) bool) *interface{} {
	for p := l.Head; p != nil; p = p.Next {
		if comp(p.Data, ref) {
			return &p.Data
		}
	}
	return nil
}
