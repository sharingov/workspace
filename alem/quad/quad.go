package quad

import (
	"github.com/01-edu/z01"
)

func PrintStr(s string) {
	for _, ch := range s {
		z01.PrintRune(rune(ch))
	}
	z01.PrintRune('\n')
}

func Quad(x, y int, NW, NE, SW, SE, hor, ver rune) {
	if x <= 0 || y <= 0 {
		return
	}
	line := make([]rune, x, x)
	top := make([]rune, x, x)
	bottom := make([]rune, x, x)
	filler := make([]rune, x, x)
	for i := range line {
		line[i] = hor
		filler[i] = ' '
	}
	copy(top, line)
	copy(bottom, line)
	top[x-1] = NE
	bottom[x-1] = SE
	top[0] = NW
	bottom[0] = SW
	filler[0] = ver
	filler[x-1] = ver
	PrintStr(string(top))
	for i := 1; i < y; i++ {
		if i == y-1 {
			PrintStr(string(bottom))
		} else {
			PrintStr(string(filler))
		}
	}
}

func QuadA(x, y int) {
	Quad(x, y, 'o', 'o', 'o', 'o', '-', '|')
}

func QuadB(x, y int) {
	Quad(x, y, '/', '\\', '\\', '/', '*', '*')
}

func QuadC(x, y int) {
	Quad(x, y, 'A', 'A', 'C', 'C', 'B', 'B')
}

func QuadD(x, y int) {
	Quad(x, y, 'A', 'C', 'A', 'C', 'B', 'B')
}

func QuadE(x, y int) {
	Quad(x, y, 'A', 'C', 'C', 'A', 'B', 'B')
}
