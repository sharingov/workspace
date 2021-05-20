package piscine

func BTreeInsertData(root *TreeNode, data string) *TreeNode {
	if root == nil {
		return &TreeNode{Data: data}
	}
	way := &root.Right
	if data < root.Data {
		way = &root.Left
	}
	*way = BTreeInsertData(*way, data)
	(*way).Parent = root
	return root
}
