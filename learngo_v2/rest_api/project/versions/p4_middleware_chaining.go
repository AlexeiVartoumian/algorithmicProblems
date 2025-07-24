package main

import (
	"crypto/tls"
	"fmt"
	"log"
	"net/http"
	mw "restapi/internal/api/middlewares"
	"time"
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
func rootHandler(w http.ResponseWriter, r *http.Request) {

	w.Write([]byte("Hello route route"))
	fmt.Println("Hello Root route")
}
func teachersHandler(w http.ResponseWriter, r *http.Request) {

	switch r.Method {
	case http.MethodGet:

		w.Write([]byte("Hello GET mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPost:
		w.Write([]byte("Hello POST mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPut:
		w.Write([]byte("Hello PUt mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPatch:
		w.Write([]byte("Hello Patch mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodDelete:
		w.Write([]byte("Hello Delete mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	}

}

func studentsHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello teachers route "))

	switch r.Method {
	case http.MethodGet:
		w.Write([]byte("Hello GET mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPost:
		w.Write([]byte("Hello POST mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPut:
		w.Write([]byte("Hello PUt mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPatch:
		w.Write([]byte("Hello Patch mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodDelete:
		w.Write([]byte("Hello Delete mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	}
}

func execsHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello teachers route "))

	switch r.Method {
	case http.MethodGet:
		w.Write([]byte("Hello GET mthoed on teacher route"))
		fmt.Println("Hello get on teachers route")
	case http.MethodPost:
		w.Write([]byte("Hello POST mthoed on teacher route"))
		fmt.Println("Hello post on teachers route")
	case http.MethodPut:
		w.Write([]byte("Hello PUt mthoed on teacher route"))
		fmt.Println("Hello put on teachers route")
	case http.MethodPatch:
		w.Write([]byte("Hello Patch mthoed on teacher route"))
		fmt.Println("Hello patch on teachers route")
	case http.MethodDelete:
		w.Write([]byte("Hello Delete mthoed on teacher route"))
		fmt.Println("Hello delete on teachers route")
	}

}
func main() {
	port := ":3000"

	cert := "cert.pem"
	key := "key.pem"

	mux := http.NewServeMux()

	mux.HandleFunc("/", rootHandler)

	mux.HandleFunc("/teachers/", teachersHandler)

	mux.HandleFunc("/students/", studentsHandler)

	mux.HandleFunc("/exec/", execsHandler)

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

	secureMux := mw.Cors(rl.Middleware(mw.ResponseTimeMiddleware(mw.SecurityHeaders(mw.Compression(mw.Hpp(hppOptions)(mux))))))

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
