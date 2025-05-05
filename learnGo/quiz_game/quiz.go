package main

import (
	"bufio"
	"encoding/csv"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
	//"strings"
)

func readFile(filePath string, timer int) string {

	fmt.Println("time stated is ", timer)
	fmt.Println(filePath)

	f, err := os.Open(filePath)
	if err != nil {
		log.Fatal("unable to read input "+filePath, err)
	}
	defer f.Close()

	// r := csv.NewReader(strings.NewReader(f))

	r := csv.NewReader(f)

	var numCorrect int = 0

	var start = time.Now()
	var total = 0
	for {
		record, err := r.Read()

		if err == io.EOF {
			break
		}
		total += 1
		var slice1, slice2 = record[0], record[1]

		// fmt.Println(record, reflect.TypeOf(record))
		// fmt.Println(record[0], "yep", record[1])
		fmt.Println("hi there what is ", slice1)

		var timeleft = fuckoff(start, timer)

		if timeleft <= 0 {
			fmt.Println("timesup")
			break
		} else if timeleft < 10 {
			fmt.Println("less than 10 seconds left ", timeleft, " remaining")
		}

		newReader := bufio.NewReader(os.Stdin)
		value, _ := newReader.ReadString('\n')

		value = strings.TrimSuffix(value, "\n")
		value = strings.TrimSuffix(value, "\r")

		fmt.Println("passing in value ", value)
		if evaluate(value, slice2) {
			numCorrect += 1
		}
	}
	fuckingguy, err := r.ReadAll()

	total += len(fuckingguy)
	fmt.Println("you got ", numCorrect, " out of ", total)
	return " "
}

func fuckoff(start time.Time, count int) int {

	var t1 = time.Now()

	var val int64 = int64(time.Duration(t1.Sub(start).Seconds()))

	return count - int(val)
}
func evaluate(slice1 string, slice2 string) bool {

	checker, _ := strconv.Atoi(slice1)
	result, _ := strconv.Atoi(slice2)
	//= strings.Split(slice1,"+")
	//var checker int
	// if strings.Contains(slice1, "+") {
	// 	var stuff = strings.Split(slice1, "+")
	// 	val1, _ := strconv.Atoi(stuff[0])
	// 	val2, _ := strconv.Atoi(stuff[1])
	// 	checker = val1 + val2
	// 	fmt.Println(checker, "is now")
	// }

	fmt.Println(checker, "is now")
	fmt.Println(checker, result)
	return checker == result

}

func main() {

	numbPtr := flag.Int("time", 30, "anint")

	newReader := bufio.NewReader(os.Stdin)

	flag.Parse()
	fmt.Println("please enter value")
	value, _ := newReader.ReadString('\n')

	value = strings.TrimSuffix(value, "\n")
	value = strings.TrimSuffix(value, "\r")
	fmt.Printf("%q\n", value)
	readFile(value, *numbPtr)

}
