package piscine

func BTreeTransplant(root, node, rplc *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root == node {
		rplc.Parent = node.Parent
		return rplc
	}
	found := BTreeTransplant(root.Left, node, rplc)
	if found != nil {
		root.Left = found
		return root
	}
	found = BTreeTransplant(root.Right, node, rplc)
	if found != nil {
		root.Right = found
		return root
	}
	return nil
}
