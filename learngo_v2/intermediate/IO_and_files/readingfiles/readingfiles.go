package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	file, err := os.Open("output.txt")

	if err != nil {
		fmt.Println("error opening file ", err)
		return
	}
	//can used anonomoours function but complex
	defer func() {
		fmt.Println("Closing open file ")
		file.Close()
	}()

	//read the contents of the opened file
	data := make([]byte, 1024) //BUFFER to read the daat into

	_, err = file.Read(data)
	if err != nil {
		fmt.Println("eeror reading data from file", err)
	}
	fmt.Println("file content: ", string(data))

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println("line", line)
	}
}
