package main

import (
	"encoding/json"
	"fmt"
	"log"
)

type Person struct {
	FirstName string `json:"first_name" db:"firstn" xml:"first"` //can combine miltiple
	LastName  string `json:"last_name,omitempty"`
	Age       int    `json:"-"` //keep struct tag lowercase no space
}

func main() {

	person := Person{FirstName: "Jane", Age: 30}

	jsonData, err := json.Marshal(person)
	if err != nil {
		log.Fatalln("Error marshalling struct:", err)
	}
	fmt.Println(string(jsonData))
}
