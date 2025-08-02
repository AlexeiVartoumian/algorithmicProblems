package router

import (
	"net/http"
	"restapi/internal/api/handlers"
)

func StudentRouter() *http.ServeMux {

	mux := http.NewServeMux()
	mux.HandleFunc("GET /students", handlers.GetStudentsHandler)
	mux.HandleFunc("GET /students/{id}", handlers.GetOneStudentHandler)

	mux.HandleFunc("POST /students", handlers.AddStudentHandler)

	mux.HandleFunc("PUT /students/", handlers.UpdateStudentHandler)
	mux.HandleFunc("PUT /students/{id}", handlers.UpdateStudentHandler)

	mux.HandleFunc("PATCH /students", handlers.PatchStudentsHandler)
	mux.HandleFunc("PATCH /students/{id}", handlers.PatchOneStudentHandler)

	mux.HandleFunc("DELETE /students", handlers.DeleteStudentHandler)
	mux.HandleFunc("DELETE /students/{id}", handlers.DeleteOneStudentHandler)

	return mux
}
