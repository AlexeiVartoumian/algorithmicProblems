package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// func caesarsCipher(s string, k int32) string {

// 	fmt.Println(s, k)

// 	for pos, char := range s {
// 		fmt.Println(strconv.QuoteRuneToASCII(char), pos)

// 	}

// 	var temp int32 = 0
// 	var str string = ""
// 	for i := 0; i < len(s); i++ {

// 		//fmt.Println(utf8.DecodeLastRune([]byte{s[i]}))

// 		val, _ := utf8.DecodeLastRune([]byte{s[i]})

// 		if val >= 65 && val <= 90 {
// 			temp = (((val - 65) + k) % 26) + 65

// 			fmt.Println(temp, string(temp))
// 			str += string(temp)
// 		} else if val >= 97 && val <= 122 {
// 			temp = (((val - 97) + k) % 26) + 97

// 			str += string(temp)
// 		} else {
// 			str += string(val)
// 		}

// 	}
// 	fmt.Println(str)
// 	return str
// }

func caesarsCipher(s string, k int32) string {

	//var temp;

	//var str;
	//var str;
	var buffer bytes.Buffer
	for i := 0; i < len(s); i++ {

		//fmt.Println(utf8.DecodeLastRune([]byte{s[i]}))

		if s[i] >= 65 && s[i] <= 90 {

			var val int32 = (((int32(s[i]) - 65) + k) % 26) + 65

			fmt.Println(val)
			buffer.WriteString(string(val))
		} else if s[i] >= 97 && s[i] <= 122 {

			var val int32 = (((int32(s[i]) - 97) + k) % 26) + 97

			fmt.Println(val)
			buffer.WriteString(string(val))
		} else {
			buffer.WriteString(string(s[i]))
		}

	}

	fmt.Println(buffer.String())
	return buffer.String()
}

func main() {

	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Enter the string to encrypt")
	s, _ := reader.ReadString('\n')
	s = strings.TrimSpace(s)

	fmt.Println("Enter the shift value (k):")
	kStr, _ := reader.ReadString('\n')
	kStr = strings.TrimSpace(kStr)
	kTemp, err := strconv.ParseInt(kStr, 10, 64)
	if err != nil {
		fmt.Println("Error parsing k:", err)
		return
	}
	k := int32(kTemp)

	result := caesarsCipher(s, k)
	fmt.Println("Encrypted result", result)
}
