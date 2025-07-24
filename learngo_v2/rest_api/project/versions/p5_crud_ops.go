package main

import (
	"crypto/tls"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	mw "restapi/internal/api/middlewares"
	"strconv"
	"strings"
	"sync"
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

// getroute on teacher gives either one teacher or all
// json tags are important posting and getting and tell the encoder/decoder what to expect for the key
type Teacher struct {
	ID        int    `json:"id,omitempty"`
	FirstName string `json:"first_name,omitempty"`
	LastName  string `json:"last_name,omitempty"`
	Class     string `json:"class,omitempty"`
	Subject   string `json:"subject,omitempty"`
}

// searching in a map is faster then in a slice
var (
	teachers = make(map[int]Teacher)
	mutex    = &sync.Mutex{}
	nextID   = 1
)

// init dummy data in mem-db
func init() {
	teachers[nextID] = Teacher{
		ID:        nextID,
		FirstName: "John",
		LastName:  "Doe",
		Class:     "9A",
		Subject:   "Math",
	}
	nextID++
	teachers[nextID] = Teacher{
		ID:        nextID,
		FirstName: "Jane",
		LastName:  "SMith",
		Class:     "10A",
		Subject:   "Algebra",
	}
	nextID++
	teachers[nextID] = Teacher{
		ID:        nextID,
		FirstName: "Jane",
		LastName:  "Doe",
		Class:     "11A",
		Subject:   "Biology",
	}
	nextID++
}

// get method old way
func GetTeachersHandler(w http.ResponseWriter, r *http.Request) {

	path := strings.TrimPrefix(r.URL.Path, "/teachers/")
	idStr := strings.TrimSuffix(path, "/")
	fmt.Println(idStr)

	if idStr == "" {
		firstName := r.URL.Query().Get("first_name")
		lastName := r.URL.Query().Get("last_name")
		teacherList := make([]Teacher, 0, len(teachers))

		for _, teacher := range teachers {
			if (firstName == "" || teacher.FirstName == firstName) && (lastName == "" || teacher.LastName == lastName) {
				teacherList = append(teacherList, teacher)
			}
		}

		// can immediately intiailize the struct right after declaring it as one off ops
		response := struct {
			Status string    `json:"status"`
			Count  int       `json:"count"`
			Data   []Teacher `json:"data"`
		}{
			Status: "success",
			Count:  len(teachers),
			Data:   teacherList,
		}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(response)
	}

	// handle path parameter
	id, err := strconv.Atoi(idStr) //atio -> alphabet to intger takes string and converts to ingeger
	if err != nil {
		fmt.Println(err)
		return
	}
	teacher, exists := teachers[id]
	if !exists {
		http.Error(w, "Teacher not found", http.StatusNotFound)
		return
	}
	json.NewEncoder(w).Encode(teacher)
}

// post operation get incoming request part of request body
func addTeacherHandler(w http.ResponseWriter, r *http.Request) {
	mutex.Lock()
	defer mutex.Unlock()

	var newTeachers []Teacher

	// need to pass in pointed value
	err := json.NewDecoder(r.Body).Decode(&newTeachers)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
	}

	addedTeachers := make([]Teacher, len(newTeachers))

	for i, newTeacher := range newTeachers {
		newTeacher.ID = nextID
		teachers[nextID] = newTeacher
		addedTeachers[i] = newTeacher
		nextID++
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)

	// can immediately intiailize the struct right after declaring it as one off ops
	response := struct {
		Status string    `json:"status"`
		Count  int       `json:"count"`
		Data   []Teacher `json:"data"`
	}{
		Status: "success",
		Count:  len(addedTeachers),
		Data:   addedTeachers,
	}
	json.NewEncoder(w).Encode(response)
}

func teachersHandler(w http.ResponseWriter, r *http.Request) {

	switch r.Method {
	case http.MethodGet:
		//https://localhost:3000/teachers/?last_name=Doe&first_name=Jane
		GetTeachersHandler(w, r)
	case http.MethodPost:
		addTeacherHandler(w, r)
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

	// rl := mw.NewRateLimiter(5, time.Minute)

	// hppOptions := mw.HPPOptions{
	// 	CheckQuery:                  true,
	// 	CheckBody:                   true,
	// 	CheckBodyOnlyForContentType: "application/x-www-form-urlencoded",
	// 	Whitelist:                   []string{"sortBy", "sortOrder", "name", "age", "class"}, //allow known fields
	// }

	//secureMux := mw.Cors(rl.Middleware(mw.ResponseTimeMiddleware(mw.SecurityHeaders(mw.Compression(mw.Hpp(hppOptions)(mux))))))

	//secureMux := applyMiddlewares(mux, mw.Hpp(hppOptions), mw.Compression, mw.ResponseTimeMiddleware, rl.Middleware, mw.Cors)

	secureMux := mw.SecurityHeaders(mux)
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

// middleware is a function that wraps an http.handler with additional functionality

type Middleware func(http.Handler) http.Handler

func ApplyMiddlewares(handler http.Handler, middlewares ...Middleware) http.Handler {

	for _, middleware := range middlewares {
		handler = middleware(handler)
	}
	return handler
}
