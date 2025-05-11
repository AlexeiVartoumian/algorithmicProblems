package sorting

import (
	"fmt"
	"strconv"
)

// DescribeNumber should return a string describing the number.
func DescribeNumber(f float64) string {
	val := strconv.FormatFloat(f, 'f', 1, 64)

	res := "This is the number " + val

	fmt.Println(res)
	return res
}

type NumberBox interface {
	Number() int
}

// DescribeNumberBox should return a string describing the NumberBox.
func DescribeNumberBox(nb NumberBox) string {

	val := nb.Number()
	return "This is a box containing the number " + strconv.Itoa(val) + ".0"
}

type FancyNumber struct {
	n string
}

func (i FancyNumber) Value() string {
	return i.n
}

type FancyNumberBox interface {
	Value() string
}

// ExtractFancyNumber should return the integer value for a FancyNumber
// and 0 if any other FancyNumberBox is supplied.
func ExtractFancyNumber(fnb FancyNumberBox) int {

	var _, ok = fnb.(FancyNumber)
	var value, _ = strconv.Atoi(fnb.Value())

	//   switch interfacetype.(type) {
	// case FancyNumberBox : return value
	//       default : return 0;

	//   }
	if ok {
		return value
	}
	return 0
}

// DescribeFancyNumberBox should return a string describing the FancyNumberBox.
func DescribeFancyNumberBox(fnb FancyNumberBox) string {

	var val = ExtractFancyNumber(fnb)
	var res = "This is a fancy box containing the number " + strconv.Itoa(val) + ".0"
	return res
}

// DescribeAnything should return a string describing whatever it contains.
func DescribeAnything(i interface{}) string {

	switch v := i.(type) {
	case int:
		return DescribeNumber(float64(v))
	case float64:
		return DescribeNumber(float64(v))
	case NumberBox:
		return DescribeNumberBox(v)
	case FancyNumberBox:
		return DescribeFancyNumberBox(v)
	default:
		return "Return to sender"
	}
}
