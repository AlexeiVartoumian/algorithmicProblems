package main

import (
	"fmt"
	"os"
)

// consider using bufio when writing large files as opposed to the base io
func main() {

	file, err := os.Create("output.txt")

	if err != nil {
		fmt.Println("Error creatign file. ", file)
		return
	}
	defer file.Close()

	data := []byte("Hello world \n")
	_, err = file.Write(data)
	if err != nil {
		fmt.Println("eeror writing to file", err)
		return
	}
	fmt.Println("data data been wrrited to file")

	file2, err := os.Create("writeString.txt")

	if err != nil {
		fmt.Println("Error crearting file", err)
		return
	}
	defer file.Close()
	file2.WriteString("hello go as a string \n")
}
