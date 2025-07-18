package main

import (
	"fmt"
	"reflect"
)

type Greeter struct{}

func (g Greeter) Greet(fname, lname string) string {
	return "Hello" + fname + " " + lname
}

func main() {
	g := Greeter{}
	t := reflect.TypeOf(g)
	v := reflect.ValueOf(g)
	var method reflect.Method

	fmt.Println("Type", t)
	for i := range t.NumMethod() {
		// lol alreday assigned so = needed
		// did := which caused a panic
		method = t.Method(i)
		fmt.Printf("Method %d %s\n", i, method.Name)

	}

	m := v.MethodByName(method.Name)
	results := m.Call([]reflect.Value{reflect.ValueOf("Alice"), reflect.ValueOf("Doe")})
	//if string then []string["alice"]
	// but here []type{type"somevalue") , type{"somevalue"}}

	fmt.Println("greet result", results[0].String())
}

type Person struct {
	Name string
	Age  int
}

func structsExample3() {

	p := Person{Name: "Alice", Age: 30}
	v := reflect.ValueOf(p)

	for i := range v.NumField() {
		fmt.Printf("Field %d %v \n", i, v.Field(i))
	}

	v1 := reflect.ValueOf(&p).Elem()

	// modifiying value of struct using reflection
	//NOTE THAT REFLECTION IS RUNNING AT RUNTIME
	//meaning private fields which are lowercase
	//CAANNOT BE ACCESSible.
	//REFLECTION enforces the same visibility as language itself
	nameField := v1.FieldByName("name")
	if nameField.CanSet() {
		nameField.SetString("Jane")
	} else {
		fmt.Println("cannot set")
	}
	fmt.Println("Modified Person", p)

}

func primitiveExample1() {

	x := 42
	v := reflect.ValueOf(x)
	t := v.Type()

	fmt.Println("Vakye of V: ", v)
	fmt.Println("Type", t)
	fmt.Println("Kind", t.Kind())
	fmt.Println("is zero", v.IsZero()) // can check zero type i.e nil of a given type

	//conditional on reflect package
	fmt.Println("is INt", t.Kind() == reflect.Int)

	y := 10
	v1 := reflect.ValueOf(&y).Elem() // getting a pointer to y and egtting the value stored at this memory address
	// otherwise we simply get the memory address

	v2 := reflect.ValueOf(&y)
	fmt.Println("V2 type : ", v2.Type())

	fmt.Println("orginal value before relfection modicatyion using reflection paclage", v1.Int())
	//using reflection to modify elem at runtime
	v1.SetInt(18)
	fmt.Println("MOdifeid value", v1.Int())

	//what about interface which is for type any ?

	var itf interface{} = "Hello"
	v3 := reflect.ValueOf(itf)
	//then do conditioanl check
	if v3.Kind() == reflect.String {
		fmt.Println("String value", v3.String())
	}
}
