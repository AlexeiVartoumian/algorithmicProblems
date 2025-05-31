package main

import "fmt"

// keep in mind that types and methods are defined in global scope
type Person struct {
	FirstName string
	LastName  string
	Age       int
}

//value reciever
func (p Person) fullName() string {
	return p.FirstName + p.LastName
}

//pointer reciver
func (p *Person) happyBirthday() int {

	p.Age++
	return p.Age
}

func main() {

	p1 := Person{
		FirstName: "tony",
		LastName:  "Babish",
		Age:       33,
	}

	fmt.Println(p1.Age)

}
