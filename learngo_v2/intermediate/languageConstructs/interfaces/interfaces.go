package main

import (
	"fmt"
	"math"
)

type Geometry interface {
	area()
	perim()
}

type Rect struct {
	width, height float64
}
type Circle struct {
	radius float64
}

func (r Rect) area() float64 {
	return r.height * r.width
}

func (c Circle) area() float64 {
	return c.radius * c.radius * math.Pi
}

func (r Rect) perim() float64 {
	return 2 * (r.height * r.width)
}

func (c Circle) perim() float64 {
	return 2 * c.radius * math.Pi
}

func printType(i interface{}) {

	switch i.(type) {
	case int:
		fmt.Println("int")

	case string:
		fmt.Println("string")

	default:
		fmt.Println("type unknown")
	}
}
