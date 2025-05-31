package main

import "fmt"

type person struct {
	Name string
	Age  int
}

// fields of embeedded struct are promtoed to
type Employee struct {
	person
	//employeeInfo person //-> if we did this then values can only be accessed through this
	EmployeeId string
	Salary     float64
}

func (p person) introduce() {
	fmt.Printf("Hi there im %s and im %d year old \t", p.Name, p.Age)
}

// overriding the the funciton
func (e Employee) introduce() {
	fmt.Printf("hi im overriding the above method im %s empid %s and i earn %.2f", e.Name, e.EmployeeId, e.Salary)
}

// only one main function per package
func execute() {

	emp := Employee{
		person:     person{Name: "tony", Age: 23},
		EmployeeId: "E001",
		Salary:     50000,
	}

	fmt.Println(emp)
	fmt.Println("Name", emp.Name)
	fmt.Println("Emp Id", emp.EmployeeId)
	fmt.Println("Salary:", emp.Salary)

	// because the employee has embedded struct person we now also can access the methods on it
	emp.introduce()

}
