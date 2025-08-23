package main

import (
	"crypto/tls"
	"embed"
	"fmt"
	"log"
	"net/http"
	"os"
	mw "restapi/internal/api/middlewares"
	router "restapi/internal/api/routers"
	"restapi/versions/project_v6/pkg/utils"
	"time"

	"github.com/joho/godotenv" //this package grabs env vars from the env file and anot the os
)

// below is eg for mac os binary
// GOOS=darwin GOARCH=arm64 go build -o rest_api_macOS_arm64 server.go

// GOOS=windows GOARCH=amd64 go build -o binaries/win/rest_api_windows_X86-64 server.go
// GOOS=linux GOARCH=amd64 go build -o binaries/win/rest_api_linux_X86-64 server.go

// not do to in prod i.e using .env file but for practise can use embd file to pass in to create a binary need to explicitly add the comment below for embed to wrk
//
//go:embed .env
var envFile embed.FS

func loadEnvFromEmbeddedFile() {
	// read the embedded .env file
	content, err := envFile.ReadFile(".env")
	if err != nil {
		log.Fatalf("error reading .envfile %v", err)
	}

	//create a temp file to loaf the variables
	tempfile, err := os.CreateTemp("", ".env")
	if err != nil {
		log.Fatalf("Error creating temp .env file %v", err)
	}
	defer os.Remove(tempfile.Name())

	//write contents of the emebded .env file to the temp file
	_, err = tempfile.Write(content)
	if err != nil {
		log.Fatalf("Error writing to temp .env file %v", err)
	}

	err = tempfile.Close()
	if err != nil {
		log.Fatalf("Error closing temp file %v", err)
		return
	}

	err = godotenv.Load()
	if err != nil {
		log.Fatalf("Error Loading envfile %v", err)
		return
	}
}

type User struct {
	Name string `json:"name"`
	Age  string `json:"age"`
	City string `json:"city"`
}

// what is mux ?
// referes to request multiplexer -> martches incoming requests to respective handler
// why use it ? allows to define multopel endpoints for api whre each route has its own
// handler function . separates logfic dor different routes.
// use mux to group related routes  or apply middleware to specific set of routes
// user mux when want to use custom handlers or middlewares

func main() {

	//define once use everywher not a production use case function is for binary
	loadEnvFromEmbeddedFile()

	// err := godotenv.Load()

	// if err != nil {
	// 	utils.ErrorHandler(err, "")
	// 	return
	// }

	port := os.Getenv("API_PORT")

	// cert := "cert.pem"
	// key := "key.pem"

	cert := os.Getenv("CERT_FILE")
	key := os.Getenv("KEY_FILE")

	tlsConfig := &tls.Config{
		MinVersion: tls.VersionTLS12,
	}

	rl := mw.NewRateLimiter(5, time.Minute)

	hppOptions := mw.HPPOptions{
		CheckQuery:                  true,
		CheckBody:                   true,
		CheckBodyOnlyForContentType: "application/x-www-form-urlencoded",
		Whitelist:                   []string{"sortBy", "sortOrder", "name", "age", "class"}, //allow known fields
	}

	//router := router.Router()
	router := router.MainRouter()
	jwtMiddleware := mw.MiddlewaresExcludePaths(mw.JWTMiddleware, "/execs/login", "/execs/forgotpassword", "/execs/resetpassword/reset")

	// prder of ops is from cors to securityheaders i.e cors fires first security headers last
	secureMux := utils.ApplyMiddlewares(router, mw.SecurityHeaders, mw.Compression, mw.Hpp(hppOptions), mw.XSSMiddleware, jwtMiddleware,
		mw.ResponseTimeMiddleware, rl.Middleware, mw.Cors)

	//secureMux := mw.JWTMiddleware(mw.SecurityHeaders(router))
	//secureMux := mw.SecurityHeaders(router)
	//secureMux := mw.JWTMiddleware(mw.SecurityHeaders(router))

	//secureMux := mw.XSSMiddleware(router)
	server := &http.Server{
		Addr: port,
		//Handler:   middlewares.SecurityHeaders(mux), // refer to middlewares.mux for diff on handler func vs handlefunc
		//Handler:   middlewares.Cors(mux),
		//Handler:   rl.Middleware(mw.Compression(mw.ResponseTimeMiddleware(mw.SecurityHeaders(mw.Cors(mux))))),
		Handler:   secureMux,
		TLSConfig: tlsConfig,
	}
	fmt.Println("server is runnong on port", port)
	err := server.ListenAndServeTLS(cert, key)

	if err != nil {
		log.Fatalln("Error starting the server")
	}

}
