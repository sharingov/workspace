package main

import (
	"io/ioutil"
	"os"

	"github.com/01-edu/z01"
)

func PrintStr(s string) {
	for _, r := range s {
		z01.PrintRune(r)
	}
}

func main() {
	args := os.Args[1:]
	for _, s := range args {
		file, err := os.Open(s)
		if err != nil {
			PrintStr("ERROR:" + err.Error()[4:])
			continue
		}
		data, err := ioutil.ReadAll(file)
		if err != nil {
			PrintStr(err.Error())
		}
		PrintStr(string(data))
		file.Close()
	}
}
