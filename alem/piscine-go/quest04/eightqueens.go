package piscine

var (
	grid    [8][8]int
	stack   []int
	current int = 0
)

func correction(x, y int, fill bool) {
	var val int
	if fill {
		stack = append(stack, y+1)
		val = 1
	} else {
		stack = stack[:len(stack)-1]
		val = -1
	}
	for i := 0; i < 8; i++ {
		grid[x][i] += val
		grid[i][y] += val
		dia1 := y + x - i
		dia2 := y - x + i
		if dia1 >= 0 && dia1 < 8 {
			grid[i][dia1] += val
		}
		if dia2 >= 0 && dia2 < 8 {
			grid[i][dia2] += val
		}
	}
}

func EightQueens() {
	if current == 8 {
		PrintlnSlice(stack)
		return
	}
	for i := 0; i < 8; i++ {
		if grid[current][i] == 0 {
			correction(current, i, true)
			current++
			EightQueens()
			current--
			correction(current, i, false)
		}
	}
}
