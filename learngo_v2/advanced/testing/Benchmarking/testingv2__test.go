package benchmarking

import "testing"

func Add(a, b int) int {
	return a + b
}

// below is structure of a test
// must follow naming pattern and have pointer to testing.T
// IMPORTANT FILE ITSELF MUST HAVE _test as suffix
// eg this file is testing_benchmark_test.go
// then can do go test testing_benchmark_test.go

func TestAddTableDriven(t *testing.T) {
	tests := []struct{ a, b, expected int }{
		{2, 3, 5},
		{0, 0, 0},
		{-1, 1, 0},
	}

	for _, test := range tests {
		result := Add(test.a, test.b)
		if result != test.expected {
			t.Errorf("Add(%d,%d) = %d; want %d", test.a, test.b, result, test.expected)
		}
	}
}

// go run testing_bench_v2.go
