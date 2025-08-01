package router

import (
	"net/http"
	"restapi/internal/api/handlers"
)

func ExecRouter() *http.ServeMux {

	mux := http.NewServeMux()
	mux.HandleFunc("GET /execs", handlers.GetExecsHandler)
	mux.HandleFunc("GET /execs/{id}", handlers.GetOneExecsHandler)
	mux.HandleFunc("GET /execs/login", handlers.LoginHandler)

	mux.HandleFunc("POST /execs", handlers.AddExecsHandler)
	mux.HandleFunc("POST /execs/login", handlers.LoginHandler)
	mux.HandleFunc("POST /execs/logout", handlers.GetExecsHandler)
	mux.HandleFunc("POST /execs/forgotpassword", handlers.GetExecsHandler)
	mux.HandleFunc("POST /execs/resetpassword/reset/{resetcode}", handlers.GetExecsHandler)
	mux.HandleFunc("POST /execs/{id}/updatepassword", handlers.GetExecsHandler)

	mux.HandleFunc("PATCH /execs/{id}", handlers.PatchOneExecHandler)
	mux.HandleFunc("PATCH /execs/", handlers.PatchExecsHandler)

	mux.HandleFunc("DELETE /execs/{id}", handlers.DeleteOneExecHandler)

	return mux
}
