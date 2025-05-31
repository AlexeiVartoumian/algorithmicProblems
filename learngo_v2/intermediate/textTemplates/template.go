package main

import (
	"bufio"
	"fmt"
	"html/template"
	"os"
	"strings"
)

func main() {

	//here we y that we care about treating this a s atemplate
	//tmpl := template.New("example")

	//here we will pull the name variable from a struct
	//tmpl, err := template.New("example").Parse("Welcome , {{.name}}! How are you doing?")

	//this way does not need a error
	// tmpl := template.Must(template.New("example").Parse("Welcome , {{.name}}! How are you doing?"))

	// // if err != nil {
	// // 	panic(err)
	// // }
	// //use a struct to populate template
	// //define data for the welcome message template , the values of map will be flexible so keep them as an interface
	// data := map[string]interface{}{
	// 	"name": "John",
	// }

	// // here os.Stdout we are writing to terminal
	// err = tmpl.Execute(os.Stdout, data)

	// if err != nil {
	// 	panic(err)
	// }

	//the below renders the templates taken from the terminal
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("Enter your name")
	name, _ := reader.ReadString('\n') // remember not a string tis need single quote

	name = strings.TrimSpace(name)
	// storing templates in map
	templates := map[string]string{
		"welcome":      "welcome, {{.name}}! We're glad you joined.",
		"notification": "{{.name}} , you have a new notification: {{.notification}}",
		"error":        "Oops! an error occured: {{.errorMessage}}",
	}
	//parse and store templates value of map is pointer because template.parse
	// returns func (t *template.Template) Parse(text string) (*template.Template, error)
	parsedTemplates := make(map[string]*template.Template)
	for name, tmpl := range templates {
		parsedTemplates[name] = template.Must(template.New(name).Parse(tmpl))

	}

	for {
		//show menu
		fmt.Println("\nMenu:")
		fmt.Println("1. Join:")
		fmt.Println("2. Get Notification:")
		fmt.Println("3. Get Error:")
		fmt.Println("4. Exit:")
		fmt.Println("Choose an option")
		choice, oops := reader.ReadString('\n')
		choice = strings.TrimSpace(choice)

		if oops != nil {
			fmt.Println("error happends", oops)
		}
		var data map[string]interface{} // here we are saying the value can be anything , losing type assertion
		var tmpl *template.Template

		switch choice {
		case "1":
			tmpl = parsedTemplates["welcome"] // make sure this matches the string value pf the key
			data = map[string]interface{}{"name": name}
		case "2":
			fmt.Println("Enter your notification message: ")
			notification, _ := reader.ReadString('\n')
			notification = strings.TrimSpace(notification)
			tmpl = parsedTemplates["notification"]
			data = map[string]interface{}{"name": name, "notification": notification} //map literal assigning on the spot

		case "3":
			fmt.Println("Enter your error message:")
			errorMessage, _ := reader.ReadString('\n')
			errorMessage = strings.TrimSpace(errorMessage)
			tmpl = parsedTemplates["error"]
			data = map[string]interface{}{"name": name, "errorMessage": errorMessage}

		case "4":
			fmt.Println("Exiting")
			return
		default:
			fmt.Println("Invalid choice. Please select a valid option")
			continue
		}

		err := tmpl.Execute(os.Stdout, data)
		if err != nil {
			fmt.Println("Error executing template", err)
		}
	}
}
