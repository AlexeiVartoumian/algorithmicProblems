package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {

	//create a new http client
	// with a reference to it
	client := &http.Client{}

	resp, err := client.Get("https://jsonplaceohlder.typicode/posts/1")
	//resp, err := client.Get("https://swapi.dev/api/people")

	if err != nil {
		fmt.Println("Error making GET request", err)
		return
	}
	// since client. get returns a pointer to http client
	// . since response struct haa many options close the body
	defer resp.Body.Close()

	// read and print the response body
	// why because response.BOdyif of type io
	//io.ReadALl returns body and error
	body, err := io.ReadAll(resp.Body)

	if err != nil {
		fmt.Println("Error reading response body", err)
		return
	}
	//body is a byte slice
	fmt.Println(string(body))

}
