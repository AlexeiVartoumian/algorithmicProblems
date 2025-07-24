package main

import (
	"fmt"
	"net/http"
)

// modern routing requires at least 1.22 in order to function
func main() {

	mux := http.NewServeMux()

	//methods based routing
	mux.HandleFunc("POST /items/create", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Item created")
	})

	mux.HandleFunc("DELETE /items/create", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Item created")
	})

	//wildcard in pattern
	mux.HandleFunc("POST /teachers/{id}", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Teacher ID: %s", r.PathValue("id"))
	})

	mux.HandleFunc("/files/{path...}", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Path ID: %s", r.PathValue("path"))
	})

	mux.HandleFunc("/path1/path2", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Path ID: %s", r.PathValue("path"))
	})

	http.ListenAndServe(":8080", mux)

}
