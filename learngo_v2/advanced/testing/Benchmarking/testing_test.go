package benchmarking

import "testing"

// func Add(a, b int) int {
// 	return a + b
// }

// below is structure of a test
// must follow naming pattern and have pointer to testing.T
// IMPORTANT FILE ITSELF MUST HAVE _test as suffix
// eg this file is testing_benchmark_test.go
// then can do go test testing_benchmark_test.go
func TestAdd(t *testing.T) {
	result := Add(2, 3)

	expected := 5
	if result != expected {
		t.Errorf("Add(2,5) = %d: want 5", result)
	}
}

// func main() {

// 	//to define a test

// }
