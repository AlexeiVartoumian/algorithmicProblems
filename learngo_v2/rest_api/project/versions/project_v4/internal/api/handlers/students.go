package handlers

import (
	"fmt"
	"net/http"
)

func StudentsHandler(w http.ResponseWriter, r *http.Request) {
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
