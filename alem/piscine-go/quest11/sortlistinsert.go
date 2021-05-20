package piscine

func SortListInsert(l *NodeI, data_ref int) *NodeI {
	var arr ints
	for l != nil {
		arr = append(arr, l.Data)
		l = l.Next
	}
	arr = append(arr, data_ref)
	arr.Sort()
	list := &ListI{}
	for _, e := range arr {
		ListIPushBack(list, e)
	}
	return list.Head
}
