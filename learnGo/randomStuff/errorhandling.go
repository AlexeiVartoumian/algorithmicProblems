package thefarm

import (
	"errors"
	"fmt"
)

// type FodderCalculator interface {
//     FodderAmount(int) (float64, error)
//     FatteningFactor() (float64 ,error)
// }

// TODO: define the 'DivideFood' function
func DivideFood(fd FodderCalculator, numCows int) (float64, error) {

	//var error  = errors.New("something went wrong")
	amount, err := fd.FodderAmount(numCows)

	if err != nil {
		//error  = errors.New("amount could not be determined")
		return 0, err
	}
	fat, err := fd.FatteningFactor()
	if err != nil {
		//error  = errors.New("factor could not be determined")
		return 0, err
	}

	return (amount * fat) / float64(numCows), nil
}

// TODO: define the 'ValidateInputAndDivideFood' function
func ValidateInputAndDivideFood(fd FodderCalculator, numCows int) (float64, error) {
	if numCows > 0 {
		return DivideFood(fd, numCows)
	}
	var error = errors.New("invalid number of cows")
	return 0, error
}

// TODO: define the 'ValidateNumberOfCows' function
type InvalidCowsError struct {
	cows    int
	details string
}

func (e *InvalidCowsError) Error() string {
	return fmt.Sprintf("%d %s", e.cows, e.details)
}

func ValidateNumberOfCows(numCows int) error {

	if numCows == 0 {
		return &InvalidCowsError{
			cows:    numCows,
			details: "cows are invalid: no cows don't need food",
		}
	}
	if numCows < 0 {
		return &InvalidCowsError{
			cows:    numCows,
			details: "cows are invalid: there are no negative cows",
		}
	}
	return nil
}

// Your first steps could be to read through the tasks, and create
// these functions with their correct parameter lists and return types.
// The function body only needs to contain `panic("")`.
//
// This will make the tests compile, but they will fail.
// You can then implement the function logic one by one and see
// an increasing number of tests passing as you implement more
// functionality.
