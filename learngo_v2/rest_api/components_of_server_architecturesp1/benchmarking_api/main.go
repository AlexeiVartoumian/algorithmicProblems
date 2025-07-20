package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Person struct {
	Name string `json:"name"`
	Age  int32  `json:"Age"`
}

// http://localhost:8080/person?id=3 for postman
// wrk -t8 -c400 -d30s "http://localhost:8080/person?id=1"
// use wrk will use 8 threads = -t8 , 400 concurrent connections
// -c = concurrent connections , duration = -d
// in terminal montior with htop
// wrk -t8 -c400 -d30s "http://wifinetworkip:8080/person?id=1"
// take note running wrk on wsl means needing to hit the ip addr of wifi see ipconfig on powershell for details
var personData = map[string]Person{
	"1": {Name: "John Doe", Age: 30},
	"2": {Name: "John Doe", Age: 28},
	"3": {Name: "John Doe", Age: 25},
}

func getPersonHandler(w http.ResponseWriter, r *http.Request) {
	//get id from url query parameters
	id := r.URL.Query().Get("id")

	if id == "" {
		http.Error(w, "ID is missing", http.StatusBadRequest)
		return
	}

	person, exists := personData[id]

	//find id send htt code
	if !exists {
		http.Error(w, "Person not found", http.StatusNotFound)
		return
	}

	//set headers
	w.Header().Set("Content-Type", "application/json")

	if err := json.NewEncoder(w).Encode(person); err != nil {
		http.Error(w, "Failed to encode response", http.StatusInternalServerError)
	}
}

func main() {

	port := 8080

	fmt.Printf("Server started on port %d\n", port)

	http.HandleFunc("/person", getPersonHandler)

	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", port), nil))
}
