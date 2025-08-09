package main

import (
	"crypto/tls"
	"fmt"
	"log"
	"net/http"
	"os"
	mw "restapi/internal/api/middlewares"
	"restapi/internal/api/repository/sqlconnect"
	router "restapi/internal/api/routers"
	"restapi/versions/project_v6/pkg/utils"

	"github.com/joho/godotenv" //this package grabs env vars from the env file and anot the os
)

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

	//define once use everywher
	err := godotenv.Load()

	if err != nil {
		utils.ErrorHandler(err, "")
		return
	}

	_, err = sqlconnect.ConnectDb()

	if err != nil {
		fmt.Println("Error----", err)
		return
	}
	port := os.Getenv("API_PORT")

	cert := "cert.pem"
	key := "key.pem"

	tlsConfig := &tls.Config{
		MinVersion: tls.VersionTLS12,
	}

	// rl := mw.NewRateLimiter(5, time.Minute)

	// hppOptions := mw.HPPOptions{
	// 	CheckQuery:                  true,
	// 	CheckBody:                   true,
	// 	CheckBodyOnlyForContentType: "application/x-www-form-urlencoded",
	// 	Whitelist:                   []string{"sortBy", "sortOrder", "name", "age", "class"}, //allow known fields
	// }

	//secureMux := mw.Cors(rl.Middleware(mw.ResponseTimeMiddleware(mw.SecurityHeaders(mw.Compression(mw.Hpp(hppOptions)(mux))))))

	//secureMux := utils.ApplyMiddlewares(mux, mw.Hpp(hppOptions), mw.Compression, mw.ResponseTimeMiddleware, rl.Middleware, mw.Cors)

	//router := router.Router()
	router := router.MainRouter()
	//jwtMiddleware := mw.MiddlewaresExcludePaths(mw.JWTMiddleware, "/execs/login", "/execs/forgotpassword", "/execs/resetpassword/reset")
	//secureMux := mw.JWTMiddleware(mw.SecurityHeaders(router))
	//secureMux := mw.SecurityHeaders(router)
	//secureMux := mw.JWTMiddleware(mw.SecurityHeaders(router))
	//secureMux := jwtMiddleware(mw.SecurityHeaders(router))
	secureMux := mw.XSSMiddleware(router)
	server := &http.Server{
		Addr: port,
		//Handler:   middlewares.SecurityHeaders(mux), // refer to middlewares.mux for diff on handler func vs handlefunc
		//Handler:   middlewares.Cors(mux),
		//Handler:   rl.Middleware(mw.Compression(mw.ResponseTimeMiddleware(mw.SecurityHeaders(mw.Cors(mux))))),
		Handler:   secureMux,
		TLSConfig: tlsConfig,
	}
	fmt.Println("server is runnong on port", port)
	err = server.ListenAndServeTLS(cert, key)

	if err != nil {
		log.Fatalln("Error starting the server")
	}

}
