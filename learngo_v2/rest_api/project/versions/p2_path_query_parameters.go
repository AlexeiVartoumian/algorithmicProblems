package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"
)

type User struct {
	Name string `json:"name"`
	Age  string `json:"age"`
	City string `json:"city"`
}

// We see that query parameters are a powerful way to pass data to our server via URLs, and the standard

// library in go provides simple and effective tools to extract and work with query parameters.

// By using these tools, we can implement features like filtering, sorting, and pagination in our web

// applications.
func rootHandler(w http.ResponseWriter, r *http.Request) {

	w.Write([]byte("Hello route route"))
	fmt.Println("Hello Root route")
}
func teachersHandler(w http.ResponseWriter, r *http.Request) {
	// teachers{id}
	// teacjers/?key=value&query=value2&sortby=email&sortorder=ASC -> query parameter often used with get reqsts vi
	switch r.Method {
	case http.MethodGet:
		fmt.Println(r.URL.Path)
		//browser applies forward slash after request need to parse
		path := strings.TrimPrefix(r.URL.Path, "/teachers/")
		userId := strings.TrimSuffix(path, "/")
		fmt.Println("The id is", userId)

		fmt.Println("Query params", r.URL.Query())
		queryParams := r.URL.Query()
		sortby := queryParams.Get("sortby")
		key := queryParams.Get("key")
		sortorder := queryParams.Get("sortorder")

		if sortorder == "" {
			sortorder = "DESC"
		}

		fmt.Printf("Sortby %v , Sort order %v , Key: %v", sortby, sortorder, key)

		w.Write([]byte("Hello GET mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPost:
		w.Write([]byte("Hello POST mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPut:
		w.Write([]byte("Hello PUt mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPatch:
		w.Write([]byte("Hello Patch mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodDelete:
		w.Write([]byte("Hello Delete mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	}
	w.Write([]byte("Hello teachers route "))

}

func studentsHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello teachers route "))

	switch r.Method {
	case http.MethodGet:
		w.Write([]byte("Hello GET mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPost:
		w.Write([]byte("Hello POST mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPut:
		w.Write([]byte("Hello PUt mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPatch:
		w.Write([]byte("Hello Patch mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodDelete:
		w.Write([]byte("Hello Delete mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	}
}

func execsHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello teachers route "))

	switch r.Method {
	case http.MethodGet:
		w.Write([]byte("Hello GET mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPost:
		w.Write([]byte("Hello POST mthoed on teacher route"))
		fmt.Println("Hello post on teachers route")
	case http.MethodPut:
		w.Write([]byte("Hello PUt mthoed on teacher route"))
		fmt.Println("Hello put on teachers route")
	case http.MethodPatch:
		w.Write([]byte("Hello Patch mthoed on teacher route"))
		fmt.Println("Hello patch on teachers route")
	case http.MethodDelete:
		w.Write([]byte("Hello Delete mthoed on teacher route"))
		fmt.Println("Hello delete on teachers route")
	}

}
func main() {
	port := ":3000"

	http.HandleFunc("/", rootHandler)

	http.HandleFunc("/teachers/", teachersHandler)

	http.HandleFunc("/students/", studentsHandler)

	http.HandleFunc("/exec/", execsHandler)

	fmt.Println("Server is running on port", port)
	err := http.ListenAndServe(port, nil)

	if err != nil {
		log.Fatalln("Error starting the server")
	}

}
