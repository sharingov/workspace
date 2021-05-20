package piscine

func Abort(a, b, c, d, e int) int {
	arr := ints{a, b, c, d, e}
	arr.Sort()
	return arr[2]
}
