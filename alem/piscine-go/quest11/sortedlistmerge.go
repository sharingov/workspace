package piscine

func SortedListMerge(n1 *NodeI, n2 *NodeI) *NodeI {
	var arr ints
	for n1 != nil {
		arr = append(arr, n1.Data)
		n1 = n1.Next
	}
	for n2 != nil {
		arr = append(arr, n2.Data)
		n2 = n2.Next
	}
	arr.Sort()
	list := &ListI{}
	for _, e := range arr {
		ListIPushBack(list, e)
	}
	return list.Head
}
