package piscine

func BTreeLevelCount(root *TreeNode) int {
	if root == nil {
		return 0
	} else {
		return Max(BTreeLevelCount(root.Left), BTreeLevelCount(root.Right)) + 1
	}
}
