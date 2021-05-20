package main

import (
	"os"

	"github.com/01-edu/z01"
)

var (
	grid    [9][9]int
	sudoku  [9][9]int
	lines   [9][9]bool
	columns [9][9]bool
	boxes   [9][9]bool
)

func printError() {
	for _, ch := range "Error" {
		z01.PrintRune(rune(ch))
	}
	z01.PrintRune('\n')
}

func printSudoku() {
	for _, line := range sudoku {
		for i, elem := range line {
			z01.PrintRune(rune(elem + 48))
			if i != 8 {
				z01.PrintRune(' ')
			}
		}
		z01.PrintRune('\n')
	}
}

func edit(i, j, k int, add bool) bool {
	a, b, c := &lines[i][k-1], &columns[j][k-1], &boxes[(i/3)*3+j/3][k-1]
	if add && (*a || *b || *c) {
		return false
	}
	*a, *b, *c = add, add, add
	if add {
		grid[i][j] = k
	} else {
		grid[i][j] = 0
	}
	return true
}

func create(args []string) bool {
	if len(args) != 9 {
		return false
	}
	for i, arg := range args {
		if len(arg) != 9 {
			return false
		}
		for j, r := range arg {
			if r >= '1' && r <= '9' {
				k := int(r - 48)
				if !edit(i, j, k, true) {
					return false
				}
			} else if r != '.' {
				return false
			}
		}
	}
	return true
}

func decide(i, j int) bool {
	if j != 8 {
		if !solve(i, j+1) {
			return false
		}
	} else if i != 8 {
		if !solve(i+1, 0) {
			return false
		}
	} else if sudoku[0][0] == 0 {
		sudoku = grid
	} else {
		return false
	}
	return true
}

func solve(i, j int) bool {
	if grid[i][j] == 0 {
		for k := 1; k <= 9; k++ {
			if edit(i, j, k, true) {
				if !decide(i, j) {
					return false
				}
				edit(i, j, k, false)
			}
		}
	} else {
		if !decide(i, j) {
			return false
		}
	}
	return true
}

func main() {
	if create(os.Args[1:]) && solve(0, 0) && sudoku[0][0] != 0 {
		printSudoku()
	} else {
		printError()
	}
}
