package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

type User struct {
	Name string `json:"name"`
	Age  string `json:"age"`
	City string `json:"city"`
}

func main() {
	port := ":3000"

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

		w.Write([]byte("Hello Root router"))
	})

	http.HandleFunc("/teachers", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello teachers route "))

		fmt.Println(r.Method) // get the request type
		switch r.Method {
		case http.MethodGet:
			w.Write([]byte("Hello GET mthoed on teacher route"))
			fmt.Println("Hello get on teachers route")
		case http.MethodPost:

			//parse form data (from x-www-form-urlencoded)
			err := r.ParseForm()

			if err != nil {
				http.Error(w, "error parsing form", http.StatusBadRequest)
				return
			}
			fmt.Println("Form", r.Form)

			// data processing need to store the value could also be a struct
			response := make(map[string]interface{})
			for k, v := range r.Form {
				response[k] = v
			}
			fmt.Println("processed response map", response)

			//raw body
			body, err := io.ReadAll(r.Body)
			if err != nil {
				return
			}
			fmt.Println("Raw Body", body)
			fmt.Println("Raw Body", string(body))
			var userInstance User // need to read into if exepcting json
			//turn into a usable go struct
			err = json.Unmarshal(body, &userInstance) // need to pass by pointer else a copy created and destroyed after creation

			if err != nil {
				return
			}

			fmt.Println(userInstance)
			fmt.Println("Recieved user name is ", userInstance.Name)

			//prepare response data
			response1 := make(map[string]interface{})
			for key, value := range r.Form {
				response[key] = value[0]
			}
			err = json.Unmarshal(body, &response1)
			if err != nil {
				return
			}
			fmt.Println("Unmarshalled json into a map", response1)

			// access the request detilas
			fmt.Println("Body", r.Body)
			fmt.Println("Form", r.Form)
			fmt.Println("Header", r.Header)
			fmt.Println("Context", r.Context())
			fmt.Println("ContextLength", r.ContentLength)
			fmt.Println("Host", r.Host)
			fmt.Println("Protocol", r.Proto)
			fmt.Println("Remote Addr", r.RemoteAddr)
			fmt.Println("Request URI", r.RequestURI)
			fmt.Println("TLS", r.TLS)
			fmt.Println("Trailer", r.Trailer)
			fmt.Println("Transer Encoding", r.TransferEncoding)
			fmt.Println("URL", r.URL)
			fmt.Println("User Agent", r.UserAgent())
			fmt.Println("port", r.URL.Port())
			fmt.Println("Scheme", r.URL.Scheme)

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

	})

	http.HandleFunc("/students", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello students route"))
		fmt.Println("hello students route")
	})

	http.HandleFunc("/exec", func(w http.ResponseWriter, r *http.Request) {

	})

	fmt.Println("Server is running on port", port)
	err := http.ListenAndServe(port, nil)

	if err != nil {
		log.Fatalln("Error starting the server")
	}

}
