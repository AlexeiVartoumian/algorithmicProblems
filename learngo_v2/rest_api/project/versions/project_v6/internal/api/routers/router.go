package router

import (
	"net/http"
)

func MainRouter() *http.ServeMux {
	//on the difference between handlers and handleFunc
	// earlier we had all the handlers in one place and used mux.HandleFunc
	// whihc accepts a string pattern and a hadnler func which applies logic see students_router.go
	// for implementation.

	// but now teacherouter returns a http.ServeMux which also has an option of handle ! we use
	// this handle for handling the handler funcs .so the code
	// tRouter.Handle is saying is that it takes a Handler not a handlerFunc. , in other
	// words we are passing the handler sRouter based on the root route.
	// so we are chaining the routes together where routes will pass thorugh teachers route and
	// then pass through the students route . notice the chaining with sRouter
	eRouter := ExecRouter()
	tRouter := TeacherRouter()
	sRouter := StudentRouter()

	sRouter.Handle("/", eRouter)
	tRouter.Handle("/", sRouter)
	return tRouter

	// mux := http.NewServeMux()
	// mux.HandleFunc("GET/", handlers.RootHandler)
	// mux.HandleFunc("/exec/", handlers.ExecsHandler)

	//return mux
}
