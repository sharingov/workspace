package piscine

func SortIntegerTable(table []int) {
	for i := 0; i < len(table)-1; i++ {
		max := i
		for j := i + 1; j < len(table); j++ {
			if table[j] < table[max] {
				max = j
			}
		}
		table[i], table[max] = table[max], table[i]
	}
}
