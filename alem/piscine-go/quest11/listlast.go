package piscine

func ListLast(l *List) interface{} {
	n := l.Tail
	if n != nil {
		return (*n).Data
	} else {
		return nil
	}
}
