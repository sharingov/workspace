package piscine

func traverse(root *TreeNode, level int, f func(...interface{}) (int, error)) bool {
	if root == nil {
		return false
	}
	if level == 1 {
		f(root.Data)
		return true
	}
	left := traverse(root.Left, level-1, f)
	right := traverse(root.Right, level-1, f)
	return left || right
}

func BTreeApplyByLevel(root *TreeNode, f func(...interface{}) (int, error)) {
	for i := 1; traverse(root, i, f); i++ {
	}
}
