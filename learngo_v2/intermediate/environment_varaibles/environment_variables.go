package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	user := os.Getenv("USER")
	home := os.Getenv("HOME")

	fmt.Println("User env var", user)
	fmt.Println("Home env var", home)

	//set keyval pair
	os.Setenv("FRUIT", "APPLE")

	for _, e := range os.Environ() {

		//like split but include extra param to specify how many substrings are required
		Kvpair := strings.SplitN(e, "=", 2)
		fmt.Println(Kvpair[0])
	}

	err := os.Unsetenv("FRUIT")
	if err != nil {
		fmt.Println("Error unsetting env variable", err)
		return
	}
}
