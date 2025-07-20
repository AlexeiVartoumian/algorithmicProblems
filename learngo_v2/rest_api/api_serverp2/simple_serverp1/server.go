package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {

	// since http vevrbs and methods not defined can send any requ3esr
	http.HandleFunc("/orders", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "handling incoming orders")
	})

	http.HandleFunc("/users", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "hadnling users")
	})

	port := 3000
	fmt.Println("Server is running on port ", port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", port), nil))
}
