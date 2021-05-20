package piscine

type NodeI struct {
	Data int
	Next *NodeI
}

type ListI struct {
	Head *NodeI
	Tail *NodeI
}

func ListIPushBack(l *ListI, data int) {
	p := l.Head
	n := &NodeI{Data: data}
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

func ListSort(l *NodeI) *NodeI {
	var arr ints
	for l != nil {
		arr = append(arr, l.Data)
		l = l.Next
	}
	arr.Sort()
	list := &ListI{}
	for _, e := range arr {
		ListIPushBack(list, e)
	}
	return list.Head
}
