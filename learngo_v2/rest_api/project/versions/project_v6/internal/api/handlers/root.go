package handlers

import (
	"fmt"
	"net/http"
)

func RootHandler(w http.ResponseWriter, r *http.Request) {

	w.Write([]byte("Welcome to school api"))
	fmt.Println("Hello Root route")
}
