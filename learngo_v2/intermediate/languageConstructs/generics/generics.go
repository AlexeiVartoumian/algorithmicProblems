package main

import "fmt"

//any{} the empty interface
// can use comparable any or own cusotm type here any is an interface
func swap[T any](a, b T) (T, T) {
	return b, a
}

type Stack[T any] struct {
	elements []T
}

func (s *Stack[T]) push(element T) {
	s.elements = append(s.elements, element)
}

func (s *Stack[T]) pop() (T, bool) {

	if len(s.elements) == 0 {
		var zero T
		return zero, false
	}

	element := s.elements[len(s.elements)-1]
	s.elements = s.elements[:len(s.elements)-1]
	return element, true
}

func (s *Stack[T]) isEmpty() bool {
	return len(s.elements) == 0
}

func main() {

	x, y := 1, 2
	x, y = swap(x, y)
	fmt.Println(x, y)
	x1, y1 := "john", "Jane"
	x1, y1 = swap(x1, y1)
	fmt.Println(x1, y1)

}
