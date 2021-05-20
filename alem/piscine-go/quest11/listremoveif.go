package piscine

func ListRemoveIf(l *List, data_ref interface{}) {
	var pre *NodeL = nil
	for p := l.Head; p != nil; p = p.Next {
		if p.Data == data_ref {
			if pre == nil {
				l.Head = p.Next
			} else {
				pre.Next = p.Next
			}
		} else {
			pre = p
		}
	}
	l.Tail = pre
}
