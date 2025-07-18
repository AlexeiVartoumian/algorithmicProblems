tsting benchmarking


for tests and benchmarks to be picked up by go the filename itself has to end with underscore test
i.e
some_test.go 
which will then be go test testing_benchmark_test.go

testing for wuality assurance
benchmarking for performance optimazations
profiling for performance analysis
- see files for commands

also subtests are like tests but with multi-threading . see subtests_test.go 
see below for benchmarks. 

go test -bench=. -benchmem bench_marking_test.go , gives memory allocation

will create prfiles with which interactive mode can be executed
will show benchmarks at function level
go test -bench=. -memprofile mem.pprof profiling_test.go|grep -v 'cpu'


interactive mode once the above pprofs have been created 
go tool pprof mem.pprof





testing = verifying expected behaviour annd meets set requirements

- idenity + fix bugs + code coorrectness
reliability , maintainability and documentaion on code behaviour

profiling
provides detailed 

write comeprehensive tests
matin test coverage
use rbenchamrking effeticl
profile regulary 