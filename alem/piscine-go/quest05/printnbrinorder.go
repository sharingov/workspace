package piscine

func PrintNbrInOrder(n int) {
	arr := bytes(Itoa(n))
	arr.Sort()
	PrintStr(string(arr))
}
