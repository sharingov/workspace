package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	if len(os.Args) == 1 {
		fmt.Println("File name missing")
		return
	} else if len(os.Args) > 2 {
		fmt.Println("Too many arguments")
		return
	}
	filename := os.Args[1]
	file, err := os.Open("../" + filename)
	if err != nil {
		fmt.Println("Error")
		return
	}
	data, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println("Error")
		return
	}
	fmt.Printf("%s", data)
	file.Close()
}
