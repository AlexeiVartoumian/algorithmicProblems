package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {

	//mkdir with relevant permissions //mkdir will create once only and will poanic if already exists
	checkError(os.Mkdir("subdir", 0755))

	//defer os.RemoveAll("subdir1")

	//can pass filepath _ path , also need to pass in byte slice in this case creating an empty file
	//and finally passsing permission
	os.WriteFile("subdir/somefile", []byte(""), 0755)

	checkError(os.MkdirAll("subdir/parent/child", 0755))
	checkError(os.MkdirAll("subdir/parent/child1", 0755))
	checkError(os.MkdirAll("subdir/parent/child2", 0755))
	checkError(os.MkdirAll("subdir/parent/child3", 0755))
	os.WriteFile("subdir/parent/file", []byte(""), 0755)
	os.WriteFile("subdir/parent/child1/file", []byte(""), 0755)

	result, err := os.ReadDir("subdir/parent")
	checkError(err)

	for _, entry := range result {
		fmt.Println(entry.Name(), entry.IsDir(), entry.Type())
	}
	//switch into the specified directort
	checkError(os.Chdir("subdir/parent/child"))
	result, err = os.ReadDir(".")
	checkError(err)

	for _, entry := range result {
		fmt.Println(entry.Name(), entry.IsDir(), entry.Type())
	}

	checkError(os.Chdir("../../.."))
	dir, err := os.Getwd() // get working directory
	checkError(err)
	fmt.Println(dir)

	//filepath.Walk and filepath.WalkDir
	pathfile := "subdir/parent/child"
	//follwoing the source codetrail the anonmous function is from here _>type WalkDirFunc func(path string, d DirEntry, err error) error
	filepath.WalkDir(pathfile, func(path string, d os.DirEntry, err error) error {

		if err != nil {
			fmt.Println("error ", err)
		}
		fmt.Println(path)
		return nil
	})

	//defer checkError(os.RemoveAll("subdir"))

}
