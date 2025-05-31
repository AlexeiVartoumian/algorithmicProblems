package main

import (
	"log"
	"os"
)

func main() {

	log.Println("this is a log message") // attomatically gives timestamp
	log.SetPrefix("INFO")

	//flags
	//log.SetFlags(log.Ldate)
	log.SetFlags(log.Ldate | log.Ltime | log.Llongfile)
	log.Println("This is a log message wiht data , time")

	infoLogger.Println("This is a info message")
	warnLogger.Println("This is a warn message")
	errorLogger.Println("This is a error message")

	// the above will output logs onto a terminal
	//but the below will output into a log file
	//depending on what flag you pass in the openfile will work in that manner . note the piping
	//i.e os.O_CREATE will create file if not exists
	//os.O_Wronly is write only
	//os.O_append add new messages to the file
	//0666 gives read and write permission to anyone
	//returns a pointer to the file and error
	file, err := os.OpenFile("app.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalf("Failed to open log file: %v ", err)
	}
	defer file.Close()

	// since we created a file to log into we now need to output to file
	debugLogger := log.New(file, "INFO", log.Ldate|log.Ltime|log.Lshortfile)
	debugLogger.Println("This ois a debug message")

	infoLogger1 := log.New(file, "INFO:", log.Ldate|log.Ltime|log.Lshortfile)
	warnLogger1 := log.New(file, "WARN:", log.Ldate|log.Ltime|log.Lshortfile)
	errorLogger1 := log.New(file, "ERROR:", log.Ldate|log.Ltime|log.Lshortfile)

	infoLogger1.Println("This is a infor message")
	warnLogger1.Println("This is an warn message")
	errorLogger1.Println("This is an error message")
}

// creates a new custom logger and can pass in custom loggers and can use them
var (
	// these three guys will output to terminal
	infoLogger  = log.New(os.Stdout, "INFO :", log.Ldate|log.Ltime|log.Lshortfile)
	warnLogger  = log.New(os.Stdout, "WARN :", log.Ldate|log.Ltime|log.Lshortfile)
	errorLogger = log.New(os.Stdout, "ERROR :", log.Ldate|log.Ltime|log.Lshortfile)
)
