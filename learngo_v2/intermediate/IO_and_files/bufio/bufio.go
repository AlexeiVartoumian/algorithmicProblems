package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

/*
on producers and consumers
fundamental difference on dat transfer reading into swith the read method availble on the reader object and the write method available on the writer object

firstly both are to do with data transfer. however the differnce is the flow of direction

Reader.Read(data) // -> bytes are being read into a empty container i.e the slice starts empty and gets filled from data from somewhere else , YOU provide the storage to read into
Writer.write() // -> bytes are being read from a full container to a destination i.e copies it from source to a destination , YOU provider the destination to copy/write into
*/
func main() {

	//now we have a budio reader object
	reader := bufio.NewReader(strings.NewReader("Hello , bufio pacalge! \n "))

	//can use for reading as well as buffered io , can do byte byte byte or line by line

	container := make([]byte, 20)

	// reader. read will read and transfer into the byte slice
	//WE ARE TRANSFERRING DATA FROM SOURCE TO A TARGET
	n, err := reader.Read(container)

	if err != nil {
		fmt.Println("error reading: ", err)
		return
	}
	fmt.Printf("Read %d bytes %s ", n, container[:n])

	//os is a write because it implements the write method as it os in turn uses os
	writer := bufio.NewWriter(os.Stdout)

	data := []byte("Hello , buidio")
	n, err2 := writer.Write(data)

	if err2 != nil {
		fmt.Println("Error writing", err)
	}
	fmt.Printf("Wrote %d bytes \n", n)

	//flush the buffer to ensure all data is wrrited to os.Stdout
	err = writer.Flush()
	if err != nil {
		fmt.Println("error flushing writer", err)
	}

	str := "this is a string \n"
	n, err = writer.WriteString(str)
	if err != nil {
		fmt.Println("error writing sting ", err)
		return
	}
	fmt.Printf("Wrote %d bytes \n", err)
	err = writer.Flush()
	if err != nil {
		fmt.Println("Eror flushing write", err)
		return
	}
	// whtas the differecne between write and write string ?
	// write is a byte slice
	// writestring we can pass a string directly
}
