package main

import (
	"encoding/base64"
	"fmt"
)

func main() {

	data := []byte("Hello , base64 encodoing ")

	encoding := base64.StdEncoding.EncodeToString(data)

	fmt.Println(encoding)

	//decode from base64
	decoded, err := base64.StdEncoding.DecodeString(encoding)

	if err != nil {
		fmt.Println("deomthing happended", err)
	}

	fmt.Println("Decoded", string(decoded)) // will need to cast to string since decode returns byte slice

	// for inputs that have / or + it the beloew can use the URLencoding since it will mess with the
	// encoding

	urlSafeEncoded := base64.URLEncoding.EncodeToString(data)

	fmt.Println("Url safe encoded", urlSafeEncoded)

}
