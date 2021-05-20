package piscine

import "github.com/01-edu/z01"

func PrintComb2() {
	for i := 0; i < 99; i++ {
		for j := i + 1; j < 100; j++ {
			f1 := i / 10
			f2 := i % 10
			s1 := j / 10
			s2 := j % 10
			z01.PrintRune(rune(f1 + 48))
			z01.PrintRune(rune(f2 + 48))
			z01.PrintRune(' ')
			z01.PrintRune(rune(s1 + 48))
			z01.PrintRune(rune(s2 + 48))
			if i == 98 && j == 99 {
				break
			}
			z01.PrintRune(',')
			z01.PrintRune(' ')
		}
	}
	z01.PrintRune('\n')
}
