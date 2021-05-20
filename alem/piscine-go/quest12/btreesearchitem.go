package piscine

func BTreeSearchItem(root *TreeNode, elem string) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Data == elem {
		return root
	}
	left := BTreeSearchItem(root.Left, elem)
	if left != nil {
		return left
	}
	right := BTreeSearchItem(root.Right, elem)
	return right
}
