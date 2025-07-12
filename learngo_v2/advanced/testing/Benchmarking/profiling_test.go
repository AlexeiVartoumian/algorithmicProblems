package benchmarking

import (
	"math/rand"
	"testing"
)

func GenerateRandomSlice(size int) []int {
	slice := make([]int, size)
	for i := range slice {
		slice[i] = rand.Intn(100)
	}
	return slice
}

func SumSlice(slice []int) int {
	sum := 0
	for _, v := range slice {
		sum += v
	}
	return sum
}

func TestGenerateRandomSLice(t *testing.T) {
	size := 100
	slice := GenerateRandomSlice(size)
	if len(slice) != size {
		t.Errorf("expected slie size %d , recived %d", size, len(slice))
	}
}

func BenchmarkGenerateRandomSlice(b *testing.B) {
	for range b.N {
		GenerateRandomSlice(1000)
	}
}

func BenchmarkSumSlice(b *testing.B) {
	slice := GenerateRandomSlice(1000)

	b.ResetTimer() // do not include the setup up of benchmark , only the operation is benchmarked
	// in this case some time is needed to generate slice in the function call above

	for range b.N {
		SumSlice(slice)
	}
}

//go test -bench=. -memprofile mem.pprof profiling_test.go|grep -v 'cpu'
//goos: windows
//goarch: amd64
//BenchmarkGenerateRandomSlice-22           110600 -> number of times function executed       11192 ns/op -> number of nano seconds per operation
//BenchmarkSumSlice-22                     7110824               147.6 ns/op
//PASS
//ok      command-line-arguments  3.592s

// can also use go tool pprof mem.pprof after
// interactive mode use command top
// interactive mode list -> shows source code + mem consumed
