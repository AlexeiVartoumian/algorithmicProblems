package router

import (
	"net/http"
	"restapi/internal/api/handlers"
)

func Router() *http.ServeMux {
	mux := http.NewServeMux()

	mux.HandleFunc("GET/", handlers.RootHandler)

	mux.HandleFunc("GET /teachers", handlers.GetTeachersHandler)
	mux.HandleFunc("GET /teachers/{id}", handlers.GetOneTeacherHandler)

	mux.HandleFunc("POST /teachers", handlers.AddTeacherHandler)

	mux.HandleFunc("PUT /teachers/", handlers.UpdateTeacherHandler)
	mux.HandleFunc("PUT /teachers/{id}", handlers.UpdateTeacherHandler)

	mux.HandleFunc("PATCH /teachers", handlers.PatchTeachersHandler)
	mux.HandleFunc("PATCH /teachers/{id}", handlers.PatchOneTeachersHandler)

	mux.HandleFunc("DELETE /teachers", handlers.DeleteTeacherHandler)
	mux.HandleFunc("DELETE /teachers/{id}", handlers.DeleteOneTeacherHandler)

	mux.HandleFunc("GET /students", handlers.GetStudentsHandler)
	mux.HandleFunc("GET /students/{id}", handlers.GetOneStudentHandler)

	mux.HandleFunc("POST /students", handlers.AddStudentHandler)

	mux.HandleFunc("PUT /students/", handlers.UpdateStudentHandler)
	mux.HandleFunc("PUT /students/{id}", handlers.UpdateStudentHandler)

	mux.HandleFunc("PATCH /students", handlers.PatchStudentsHandler)
	mux.HandleFunc("PATCH /students/{id}", handlers.PatchOneStudentHandler)

	mux.HandleFunc("DELETE /students", handlers.DeleteStudentHandler)
	mux.HandleFunc("DELETE /s/{id}", handlers.DeleteOneStudentHandler)

	mux.HandleFunc("/exec/", handlers.ExecsHandler)

	return mux
}
