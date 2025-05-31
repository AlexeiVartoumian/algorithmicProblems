package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	relativePath := "./data/file.txt"
	joinedPath := filepath.Join("Documents", "algorithmicProblems", "learngo_v2", "file_paths", "file.zip")
	fmt.Println("Joined path", joinedPath)

	normalizedPath := filepath.Clean("./data/../data/file.txt")
	fmt.Println("Normalized path:", normalizedPath)

	dir, file := filepath.Split("/homes/user/docs/file.txt")
	fmt.Println("File", file)
	fmt.Println("Dir", dir)
	fmt.Println(filepath.Base("/homes/user/docs/"))

	//get extension type of the file
	fmt.Println(filepath.Ext(file))
	fmt.Println(strings.TrimSuffix(file, filepath.Ext(file)))

	//get file relative to input filepath
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err != nil {
		panic(err)
	}
	fmt.Println(rel)

	//get absolute path
	abspath, err := filepath.Abs(relativePath)

	if err != nil {
		fmt.Println("ho", err)
	} else {
		fmt.Println("Absolute path", abspath)
	}
}
