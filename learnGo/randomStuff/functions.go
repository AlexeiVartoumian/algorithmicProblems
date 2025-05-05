package lasagna

//import ( "slices" )

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, minutes int) int {
	//defaultMinutes := 2
	if minutes == 0 {
		minutes = 2
	}
	return len(layers) * minutes
}

// // TODO: define the 'Quantities()' function
// func Quantities( layers []string ) (int , float64) {

//     seq1 := func ( yield func(string) bool) {
//         for _ , v := range layers {
//             if v == "sauce" {
//                 if !yield(v){
//                     return
//                 }
//             }
//         }
//     }
//     seq2 := func (  yield func(string) bool) {
//         for _ , v := range layers {
//             if v == "noodles" {
//                 if !yield(v){
//                     return
//                 }
//             }
//         }
//     }
//     val1 :=  len(slices.Collect(seq2)) * 50
//     val2 := float64( len( slices.Collect(seq1)) ) * 0.2
//     return  val1 , val2
// }
func Quantities(layers []string) (int, float64) {
	noodlesCount := 0
	sauceCount := 0

	for _, v := range layers {
		if v == "noodles" {
			noodlesCount++
		}
		if v == "sauce" {
			sauceCount++
		}
	}

	val1 := noodlesCount * 50
	val2 := float64(sauceCount) * 0.2

	return val1, val2
}

//https://pkg.go.dev/slices#Collect
// below is a higher order function that based on the predicate will do whatever I BLODDYWELLLSSY!

// func Quantities(layers []string) (int ,float64) {

//     create := func(ingredient string) func( yield func(string)  bool ) {
//         return func(yield func(string) bool){
//         for _, v := range layers {
//             if v != ingredient {
//                 if !yield(v){
//                     return
//                 }
//             }
//         }
//             }
//     }
//     return slices.Collect(create("sauce"))*0.2 , slices.Collect(create("noodles")) *50
// }
// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredientpointerStyle(friendsList []string , myList *[]string ){
    (*myList)[len(*myList)-1] = friendsList[len(friendsList)-1]
}

//useing the above
friendsList := []string{"noodles", "sauce", "mozzarella", "kampot pepper"}
	myList := []string{"noodles", "meat", "sauce", "mozzarella", "?"}

	AddSecretIngredient(friendsList, &myList) // <= THIIIIIIIIIIIIIS 
	fmt.Println(myList)


func AddSecretIngredient(friendsList, myList []string) {
	myList[len(myList)-1] = friendsList[len(friendsList)-1]
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, portions int) []float64 {

	// seq := func( yield func(float64) bool ) {

	//     for _ , v := range quantities {
	//         v =  (v / 2.0 ) * float64(portions)
	//         if !yield(v){
	//             return
	//         }
	//     }
	// }

	// return slices.Collect(seq)
	result := make([]float64, len(quantities))

	for i, v := range quantities {
		result[i] = (v / 2.0) * float64(portions)
	}

	return result
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.



You can edit this code!
Click here and start typing.
package main

import (
	"fmt"
	"slices"
)

func Quantities(layers []string) (int, float64) {

	create := func(ingredient string) func(yield func(string) bool) {
		return func(yield func(string) bool) {
			for _, v := range layers {
				if v == ingredient {
					if !yield(v) {
						return
					}
				}
			}
		}
	}
	return len(slices.Collect(create("noodles"))) * 50, float64(len(slices.Collect(create("sauce")))) * 0.2
}
func ScaleRecipe(quantities []float64, portions int) []float64 {

	seq := func(yield func(float64) bool) {

		for _, v := range quantities {
			v = (v / 2.0) * float64(portions)
			if !yield(v) {
				return
			}
		}
	}

	return slices.Collect(seq)
}

func AddSecretIngredient(friendsList []string, myList *[]string) {
	(*myList)[len(*myList)-1] = friendsList[len(friendsList)-1]
}

func main() {
	fmt.Println("Hello, 世界")
	fmt.Println(Quantities([]string{"sauce", "noodles", "sauce", "meat", "mozzarella", "noodles"}))
	quantities := []float64{1.2, 3.6, 10.5}
	scaledQuantities := ScaleRecipe(quantities, 4)
	fmt.Println(scaledQuantities)
	friendsList := []string{"noodles", "sauce", "mozzarella", "kampot pepper"}
	myList := []string{"noodles", "meat", "sauce", "mozzarella", "?"}

	AddSecretIngredient(friendsList, &myList)
	fmt.Println(myList)
}