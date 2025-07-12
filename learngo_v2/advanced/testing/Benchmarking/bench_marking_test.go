package benchmarking

import "testing"

func Add1(a, b int) int {
	return a + b
}

// to run a benchmark its a different flag to test
//go test -bench=. bench_marking.go -> specific file
// go test -bench=. will run all bench mark funcs
// like tests with testing.T need testing.B
// and to actually run it b.N where N is whats picked up by the flag
func BenchmarkAdd(b *testing.B) {
	for range b.N {
		Add1(2, 3)
	}
}

//go test -bench=. bench_marking_test.go|grep -v 'cpu' returns follwing params without cpu details
//goos: windows
//goarch: amd64 -> architecture x64 amd
//BenchmarkAdd-22 -> number of cores that system has       1000000000  -> number of iterations function was called during benchmark        0.1325 ns/op -> average time taken per operation to execute the add function
//PASS -> successful bench
//ok      command-line-arguments  0.507s -> total time taken to run the function

// can also run the memory usage of func with -benchmem flag
//go test -bench=. -benchmem bench_marking_test.go , gives memory allocation
// 0 B/op bytes per op 0 allics/op allcoation per operation
func BenchmarkAddMediumInput(b *testing.B) {

	for range b.N {
		Add(200, 300)
	}
}
