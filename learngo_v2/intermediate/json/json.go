package main

import (
	"encoding/json"
	"fmt"
	"log"
)

// struct field tags below backtick
// we are rpvoding metadata abou the feilds useful for converting the structs into json
// or feeding information into database . struct tags are good
type Person struct {
	FirstName string  `json:"first_name"`    //mention the json field in double quotes json package looks for struct tag and then double qutoes
	Age       int     `json:"age,omitempty"` // tags can be used for object relation management for example `db: "user_id"`
	Email     string  `json:"email"`
	Address   Address `json: "address"`
	//note that omitempty will not include the key of the kson value
}

type Address struct {
	City  string `json:"city"` //no space where json struct tag is done
	State string `json:"state"`
}

// when the struct is marshalled into json we are mentioning the field hat needs to be there

func main() {

	person := Person{FirstName: "John", Age: 30}

	jsonData, err := json.Marshal(person)

	if err != nil {
		fmt.Println("oops error marshalling data", err)
		return
	}
	//marshal returns  bytes
	fmt.Println(jsonData)
	fmt.Println(string(jsonData))

	person2 := Person{FirstName: "tony", Age: 30, Email: "someemail@gmail.com", Address: Address{City: "New York", State: "Albany"}}

	json2, err := json.Marshal(person2)
	if err != nil {
		fmt.Println("Error marshalling to JSON", err)
		return
	}
	fmt.Println(json2)

	//here we are marshalling into json
	//remember to use backticks where several double quote marks are being used
	jsonData1 := `{"full_name": "Jenny Doe", "emp_id": "0009", "age":30 , "address": {"city": "San Jose", "state": "CA"}}`

	var employeeFromJson Employee
	err = json.Unmarshal([]byte(jsonData1), &employeeFromJson) // need to pass the orginal variable by passing the location of the vriable

	if err != nil {
		fmt.Println("Error unmarhsalling JSON ", err)
		return
	}
	fmt.Println(employeeFromJson)
	fmt.Println("Jennys age increased by 5 years", employeeFromJson.Age+5)
	fmt.Println("Jennys city ", employeeFromJson.Address.City)

	//handling where many need to be marshalled
	listOfCityState := []Address{
		{City: "New York", State: "NY"},
		{City: "San Jose", State: "CA"},
		{City: "Las Vegas", State: "NV"},
		{City: "Modesto", State: "CA"},
		{City: "Clearwater", State: "FL"},
	}

	fmt.Println(listOfCityState)
	jsonList, err := json.Marshal(listOfCityState)
	if err != nil {
		log.Fatalln("error marshalling to json ", err)
	}
	fmt.Println("JSON List", string(jsonList))

	//handling unknown json structures // pass it into a map of interface type any
	jsondata2 := `{"name": "John", "age":30 , "address": {"city": "New York", "state": "NY"}}`
	var data map[string]interface{}

	err = json.Unmarshal([]byte(jsondata2), &data)
	if err != nil {
		log.Fatalln("Error Unmarhsaling Json", err)
	}
	fmt.Println("Decoded/Unamrshalled JSON:", data)
	fmt.Println("Decoded/Unamrshalled JSON:", data["address"])
	fmt.Println("Decoded/Unamrshalled JSON:", data["name"])
}

type Employee struct {
	FullName string  `json:"full_name"`
	EmpID    string  `json:"emp_id"`
	Age      int     `json:"age"`
	Address  Address `json:"address"`
}
