package benchmarking

import (
	"fmt"
	"testing"
)

// func Add2(a, b int) int {
// 	return a + b
// }

func TestAddSubtests(t *testing.T) {
	tests := []struct{ a, b, expected int }{
		{2, 3, 5},
		{0, 0, 0},
		{-1, 1, 0},
	}

	for _, test := range tests {
		t.Run(fmt.Sprintf("Add(%d,%d)", test.a, test.b), func(t *testing.T) {
			result := Add(test.a, test.b)
			if result != test.expected {
				t.Errorf("result = %d; want %d", result, test.expected)
			}
		})
	}
}
