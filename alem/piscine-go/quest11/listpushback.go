package piscine

func ListPushBack(l *List, data interface{}) {
	p := l.Head
	n := &NodeL{Data: data}
	l.Tail = n
	if p == nil {
		l.Head = n
		return
	}
	for p.Next != nil {
		p = p.Next
	}
	p.Next = n
}
