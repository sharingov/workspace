package piscine

func ListPushFront(l *List, data interface{}) {
	n := &NodeL{Data: data, Next: l.Head}
	l.Head = n
	if l.Tail == nil {
		l.Tail = n
	}
}
