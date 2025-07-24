package router

import (
	"net/http"
	"restapi/internal/api/handlers"
)

func Router() *http.ServeMux {
	mux := http.NewServeMux()

	mux.HandleFunc("/", handlers.RootHandler)

	mux.HandleFunc("GET /teachers/", handlers.GetTeachersHandler)
	mux.HandleFunc("GET /teachers/{id}", handlers.GetOneTeacherHandler)

	mux.HandleFunc("POST /teachers/", handlers.AddTeacherHandler)

	mux.HandleFunc("PUT /teachers/", handlers.UpdateTeacherHandler)
	mux.HandleFunc("PUT /teachers/{id}", handlers.UpdateTeacherHandler)

	mux.HandleFunc("PATCH /teachers/", handlers.PatchTeachersHandler)
	mux.HandleFunc("PATCH /teachers/{id}", handlers.PatchOneTeachersHandler)

	mux.HandleFunc("DELETE /teachers/", handlers.DeleteTeacherHandler)
	mux.HandleFunc("DELETE /teachers/{id}", handlers.DeleteOneTeacherHandler)

	mux.HandleFunc("/students/", handlers.StudentsHandler)

	mux.HandleFunc("/exec/", handlers.ExecsHandler)

	return mux
}
