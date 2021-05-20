package piscine

func ListReverse(l *List) {
	cur := l.Head
	var pre *NodeL = nil
	for cur != nil {
		jump := cur.Next
		cur.Next = pre
		pre = cur
		cur = jump
	}
	l.Head = pre
}
