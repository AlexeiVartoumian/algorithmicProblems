
modules are collections of related go packages
- versioin
- reproducibility
- organizational clarity
key commands for working with modules

go mod file is equatable with te package.json file in node js , which has version + other metadata on api


whats the difference between a package and a module ?
package is smallest unit of code organization and groups together go files consisiting of variables typs functions 
module is a collection of pacakges and is used to manage and version a group of related packages

module is defined by prescense of a mod file
- pacakges promode code resuse 
- modules group them an dversion them . package cannot exist independently .
- the standard library itself is a module with many packages contained within

- go mod init "name of module" -> will be the blue print of module contains  module name and list of dependencies
- go mod tidy -> used to manage the external dependencies i.e http2s if not used will remove it
- go get -> go get golang.org/x/net/http2 . keep in mind that getting some modules will also incorporate thier dependencies into the mod file. 
futher to this dependednices do not get stored in the project folder . they are downloaded onto the machine
where if the progect is moved a go tidy will download whats needed
- go build
- go run
- go list all -> lists all the depenendcies
- go list -m all -> lists direct and indirect depenencies

commands ran
go mod init simpleapimodule
go get golang.org/x/net/http2
go mod tidy

to build a binary

go build -o name_of_binary.exe accesspoint.go

eg
go buil -o rest_api server.go

the above build command will only run on the same operating system and architect .
if we want it to be interoperable then below flags
operating system acecepts many -> linux , macos/darwin , windows , bsd , open bsd
and architect is good for - amd64 (64-bit x86 ) = intel + amd then arm 32-bit ARM and arm64(64-bit ARM)

below is eg for mac os binary
GOOS=darwin GOARCH=arm64 go build -o rest_api_macOS_arm64 server.go

GOOS=windows GOARCH=amd64 go build -o binaries/win/rest_api_windows_X86-64 server.go
GOOS=linux GOARCH=amd64 go build -o binaries/win/rest_api_linux_X86-64 server.go

to obfuscate binaries can use below packages
also go install mvdan.cc/garble@latest
garble build [build flags] [packages]
garble build -o rest_api_server.go