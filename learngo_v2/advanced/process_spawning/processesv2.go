package main

import (
	"fmt"
	"io"
	"os"
	"os/exec"
	"strings"
	"time"
)

func main() {
	// eg 1
	// cmd := exec.Command("printenv", "SHELL")

	// output, err := cmd.Output()

	// if err != nil {
	// 	fmt.Println("Error", nil)
	// 	return
	// }
	// fmt.Println("Output", string(output))
	// -----------------------------------

	//eg2 concurrent , set the command to execute on cmd.Stdin
	// then have a pipereader with the pipereader set to cmd.stdin
	// in this way the goroutine accepting the pipewriter will
	//feed the output + executed command where cmd.Output() captures commands output after it processes input
	pipereader, pipewriter := io.Pipe()

	cmd := exec.Command("grep", "foo")
	cmd.Stdin = pipereader

	go func() {
		defer pipewriter.Close()
		pipewriter.Write([]byte("food is good\nbar\nbaz\n"))
		go func() {
			defer pipewriter.Close()
			for _, arg := range os.Args[1:] {
				pipewriter.Write([]byte(arg + "\n"))
			}
		}()
		// below are examples of how pipewriter can be used within the go routine .
		// 2. Read from a File
		// go func() {
		// 	defer pipewriter.Close()
		// 	file, err := os.Open("input.txt")
		// 	if err != nil {
		// 		return
		// 	}
		// 	defer file.Close()

		// 	io.Copy(pipewriter, file)
		// }()
		// 3. Read from Stdin
		// go func() {
		// 	defer pipewriter.Close()
		// 	io.Copy(pipewriter, os.Stdin)
		// }()
		// 4. Output from Another Command
		// go func() {
		// 	defer pipewriter.Close()
		// 	cmd2 := exec.Command("ls", "-la")
		// 	output, err := cmd2.Output()
		// 	if err != nil {
		// 		return
		// 	}
		// 	pipewriter.Write(output)
		// }()
		// 5. HTTP Response
		// go func() {
		// 	defer pipewriter.Close()
		// 	resp, err := http.Get("https://example.com")
		// 	if err != nil {
		// 		return
		// 	}
		// 	defer resp.Body.Close()

		// 	io.Copy(pipewriter, resp.Body)
		// }()
		// 6. Generate Data Programmatically
		// go func() {
		// 	defer pipewriter.Close()
		// 	for i := 0; i < 100; i++ {
		// 		line := fmt.Sprintf("line %d with foo\n", i)
		// 		pipewriter.Write([]byte(line))
		// 	}
		// }()
	}()

	output, err := cmd.Output()
	if err != nil {
		fmt.Println("Error", err)
		return
	}
	fmt.Println("Output", string(output))

	//example 3
	// cmd2 := exec.Command("ls", "-l")

	// //this time run combined stdout and errer
	// output, err := cmd2.CombinedOuput()

	// if err != nil {
	// 	fmt.Println("erreor", err)
	// 	return
	// }
	// fmt.Println("Output", string(output))

}

func time_intensive_processes() {

	cmd := exec.Command("sleep", "5")

	err := cmd.Start()

	if err != nil {
		fmt.Println("Error", err)
		return
	}

	// // process will not continute since Wait is blocking in nature
	// err = cmd.Wait()
	// if err != nil {
	// 	fmt.Pringln("error waiting", err)
	// 	return
	// }
	// fmt.Println("Process finsihed waiting")

	// here we simulate a process that takes too long and must be kiled
	time.Sleep(2 * time.Second)
	err = cmd.Process.Kill()
	if err != nil {
		fmt.Println("error killing process", err)
	}
	fmt.Println("Prcoess Killed")

}

func feeding_input_into_standard_input() {

	// like python sub process
	cmd := exec.Command("grep", "foo")

	cmd.Stdin = strings.NewReader("foo\nbar\nbaz\n")

	output, err := cmd.Output()

	if err != nil {
		fmt.Println("error", err)
		return
	}

	fmt.Println("Output", string(output))
}
