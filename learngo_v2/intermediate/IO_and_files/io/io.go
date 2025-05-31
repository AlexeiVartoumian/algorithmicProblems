package main

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

// io.Reader is a interface
func readFromReader(r io.Reader) {

	buf := make([]byte, 1024)
	n, err := r.Read(buf) //needs the byte slice buffer that it reads to read into
	if err != nil {
		log.Fatalln("Error reading from reader", err)
	}

	fmt.Println(string(buf))     // what if we no need all bytes only 800? //convert related type
	fmt.Println(string(buf[:n])) // then cut the slice!
}

func writeToWriter(w io.Writer, data string) {
	_, err := w.Write([]byte(data))
	if err != nil {
		log.Fatalln("Error reading from reader", err)
	}
}

// if we can read or write then the resource must be closed can define the interface argurmnet below in their own way
func closeResource(c io.Closer) {
	err := c.Close()
	if err != nil {
		log.Fatalln("Error reading from reader", err)
	}
}

// print an output to a screen
func bufferExample() {
	var buf bytes.Buffer //allocates a bytes.buffer instance directly creates memory on the stack
	// unless managed by go runtime or part of struct then on the heap
	buf.WriteString("Hello BUffer!") //using writer.write under the hood
	fmt.Println(buf.String())
}

func multiReaderExample() {
	r1 := strings.NewReader("Hello")
	r2 := strings.NewReader("Worlds")
	mr := io.MultiReader(r1, r2) //variadic can give as many arguemnts as wish

	//because we are creating a multireader we MUST CREATE A POINTER to DIFFERENT TO LINE 41
	buf := new(bytes.Buffer) // this will allocate memory on the heap
	_, err := buf.ReadFrom(mr)

	if err != nil {
		log.Fatalln("error reading from", err)
	}
	fmt.Println(buf.String())
}

func pipeExample() {
	pipe_reader, pipe_writer := io.Pipe()

	//because go routine needs to be executed immediately and anonymous
	//go function extracts this function out of the main thread so if the function will take 30 minutes
	//the next staement will not take 30 minutes, go func will be extracted away from main thread  and exceution will
	// will fall on the next line then once go func is compelted it will then come back to the main thread
	go func() {
		pipe_writer.Write([]byte("Hello Pipe")) //writer is going to write and store data
		pipe_writer.Close()                     // need to close the writer
	}()
	// similar to conecpt of proimises and async await in how function is taken away from main thread

	//inshort the excution below will happen without waiting for go func above to finish
	buf := new(bytes.Buffer)  // -> create pointer to buffer
	buf.ReadFrom(pipe_reader) // read will reader the data from writer and output it
	fmt.Println(buf.String())
}

func writeToFile(filepath string, data string) {
	file, err := os.OpenFile(filepath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatalln("Error openeing creating file")
	}
	defer closeResource(file)

	_, err = file.Write([]byte(data))
	if err != nil {
		log.Fatalln("error opening file", err)
	}

	// keeping in mind many packages implemnent io interfaces
	//alternate way of doing above can convert related types
	// writer := io.Writer(file) // since io.Writer and file is os.File they imple same interface

	// // writer is now the variables that holds file

	// _ , err = writer.Write([]byte(data)) // keep in mind this only has function definition need to imlpe by passing in

	// if err != nil {
	// 	log.Fatalln("Error opening/creating file",err)
	// }
}

func main() {

	fmt.Println("=== Read from Reader")
	readFromReader(strings.NewReader("Hello reader!")) // can be a file but for demo is srtin

	fmt.Println("=== Write to writer")
	var writer bytes.Buffer
	writeToWriter(&writer, "Hello Writer")
	fmt.Println(writer.String())

	fmt.Println("=== mutli reader exmaple ===")
	bufferExample()

	//io.pipe returns a reader and a writer TWO DIFFERENT RETURN VALUES
	//FURTHERMORE THEY ARE BOTH CONNECTED
	fmt.Println("=== pipe example ===")
	pipeExample()

	filepath := "io.txt"
	writeToFile(filepath, "Hello File!")

	resource := &MyResource{name: "Test resource"}
	closeResource(resource)
}

type MyResource struct {
	name string
}

// no the struct implments the close interface since it returns error
// what this means is the the closeResource function defined way up top will accept the
// myresource struct and close it
func (m MyResource) Close() error {
	fmt.Println("Closing resource", m.name)
	return nil
}
