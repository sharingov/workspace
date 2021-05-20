package piscine

func ListAt(l *NodeL, pos int) *NodeL {
	p := l
	for i := 0; i < pos; i++ {
		if p == nil {
			return nil
		}
		p = p.Next
	}
	return p
}
