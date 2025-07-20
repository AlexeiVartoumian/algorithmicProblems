package main

import (
	"fmt"
	"log"
	"net/http"
)

// for implementing servers with variadic functions as opposed to a config struct
// for options see below weblink
// https://dave.cheney.net/2014/10/17/functional-options-for-friendly-apis
func main() {

	// need to configure an endpoint to recieve requests handle func
	// accepts a function as a param
	http.HandleFunc("/", func(resp http.ResponseWriter, req *http.Request) {
		// since http.ResponseWrite is of type io as in interface
		//Fprintline accepts io.writer
		fmt.Fprintln(resp, "Hello Server")
	})

	// speicify host address and port to listen to,
	// universally above is lcoalhost addr for exrtenal request
	// doesnt have to be explicitly set by default listents on this host
	// can make more dymanic by setting the port instaed
	const serverAddr string = "127.0.0.1:3000"

	// listen and serve accepts address and http hadler
	err := http.ListenAndServe(serverAddr, nil)
	if err != nil {
		log.Fatalln("error stating server")
	}
}
