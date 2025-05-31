package main

import "github.com/sirupsen/logrus"

//go mod init nameof module
//go mod tidy
//go get packageofyourchoice
func main() {

	log := logrus.New()

	log.SetLevel(logrus.InfoLevel)

	//set log
	log.SetFormatter(&logrus.JSONFormatter{})

	//Logging examples
	log.Info("This is an infor message")
	log.Warn("This is an warning message")
	log.Error("This is a error message")

	// can use for structued logging ggod for parsing & anlying logs programatically
	// can ingest json logs with elastic search and helps with data interchange
	log.WithFields(logrus.Fields{
		"username": "John Doe",
		"method":   "GET",
	}).Info("User logged in.")
}
