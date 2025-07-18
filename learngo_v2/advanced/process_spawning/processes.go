package processes

import (
	"fmt"
	"os/exec"
)

func example() {

	cmd := exec.Command("echo", "Hello world")

	output, err := cmd.Output() // refer to function methods for return values here its byte
	if err != nil {
		fmt.Println("error", err)
		return
	}
	fmt.Println("Output", string(output))

}
