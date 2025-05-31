package main

import "fmt"

func main() {

	sequence := adder()

	// sequence type is the inner function
	fmt.Println(sequence())
	fmt.Println(sequence())
	fmt.Println(sequence())
	fmt.Println(sequence())

	//assigned and exceuted
	// order of operations
	// the outer function gets executed immediately.
	// because there is an inner function the assigned variable now contains a reference to this
	// therefore an argument can be passed to it
	subtracter := func() func(int) int {

		countdown := 99
		return func(x int) int {
			countdown -= x
			return countdown
		}
	}() // anonymous funciton that is immediately excuted

	//function calls are now stored and executed here -> in other words , we are not calling the outer function but the inner one
	//because its executed immeditale
	fmt.Println(subtracter(1))
	fmt.Println(subtracter(2))
	fmt.Println(subtracter(3))
	fmt.Println(subtracter(4))

}

// our function here returns another function , note the return type and the function has its own return type
func adder() func() int {

	i := 0 // store at memory address 0x1000
	fmt.Println("Previous value of i : ", i)

	//function with no name is an anonymous function.
	return func() int {
		i++ //(*reference to memory address 0x1000) and add it
		fmt.Println("added 1 to i ")
		return i
	}
}
