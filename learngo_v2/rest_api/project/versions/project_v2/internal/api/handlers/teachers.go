package handlers

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"restapi/internal/api/repository/sqlconnect"
	"restapi/models"
	"strconv"
	"strings"
	"sync"
)

// searching in a map is faster then in a slice
var (
	teachers = make(map[int]models.Teacher)
	mutex    = &sync.Mutex{}
	nextID   = 1
)

// init dummy data in mem-db
func init() {
	teachers[nextID] = models.Teacher{
		ID:        nextID,
		FirstName: "John",
		LastName:  "Doe",
		Class:     "9A",
		Subject:   "Math",
	}
	nextID++
	teachers[nextID] = models.Teacher{
		ID:        nextID,
		FirstName: "Jane",
		LastName:  "SMith",
		Class:     "10A",
		Subject:   "Algebra",
	}
	nextID++
	teachers[nextID] = models.Teacher{
		ID:        nextID,
		FirstName: "Jane",
		LastName:  "Doe",
		Class:     "11A",
		Subject:   "Biology",
	}
	nextID++
}

func TeachersHandler(w http.ResponseWriter, r *http.Request) {

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

// get method old way
func GetTeachersHandler(w http.ResponseWriter, r *http.Request) {

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		http.Error(w, "Error connecting to databae", http.StatusInternalServerError)
	}
	defer db.Close()

	path := strings.TrimPrefix(r.URL.Path, "/teachers/")
	idStr := strings.TrimSuffix(path, "/")
	fmt.Println(idStr)

	if idStr == "" {
		firstName := r.URL.Query().Get("first_name")
		lastName := r.URL.Query().Get("last_name")
		teacherList := make([]models.Teacher, 0)
		//teacherList := make([]models.Teacher, 0, len(teachers))

		// for _, teacher := range teachers {
		// 	if (firstName == "" || teacher.FirstName == firstName) && (lastName == "" || teacher.LastName == lastName) {
		// 		teacherList = append(teacherList, teacher)
		// 	}
		// }

		//handle multple gets on db query
		//if sure to get one result then use db.Queryrow else use db.Query for multiple results
		query := "SELECT id , first_name , last_name, email , class , subject FROM teachers WHERE 1=1"
		var args []interface{}

		if firstName != "" {
			//modifying the original query to add
			query += " AND first_name = ?"
			args = append(args, firstName)
		}
		if lastName != "" {
			query += " AND last_name = ?"
			args = append(args, lastName)
		}
		//query accepts a variadic number of argimets
		rows, err := db.Query(query, args...)

		if err != nil {
			fmt.Println(err)
			http.Error(w, "Db query error", http.StatusInternalServerError)
			return
		}
		defer rows.Close()

		for rows.Next() {
			var teacher models.Teacher
			err := rows.Scan(&teacher.ID, &teacher.FirstName, &teacher.LastName, &teacher.Email, &teacher.Class, &teacher.Subject)

			if err != nil {
				http.Error(w, "error scanning db results", http.StatusInternalServerError)
				return
			}
			teacherList = append(teacherList, teacher)

		}

		// can immediately intiailize the struct right after declaring it as one off ops
		response := struct {
			Status string           `json:"status"`
			Count  int              `json:"count"`
			Data   []models.Teacher `json:"data"`
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

	var teacher models.Teacher

	//query row will yield a result where scan accepts variadic parameters
	err = db.QueryRow("SELECT id , first_name , last_name ,email, class , subject FROM teachers WHERE id = ?", id).Scan(&teacher.ID, &teacher.FirstName,
		&teacher.LastName, &teacher.Email, &teacher.Class, &teacher.Subject)

	if err == sql.ErrNoRows {
		http.Error(w, "TEacher not found", http.StatusNotFound)
		return
	} else if err != nil {
		http.Error(w, "Database query ", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-type", "application/json")

	json.NewEncoder(w).Encode(teacher)
}

// post operation get incoming request part of request body
func addTeacherHandler(w http.ResponseWriter, r *http.Request) {
	// mutex.Lock()
	// defer mutex.Unlock()

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		http.Error(w, "Error connecting to databae", http.StatusInternalServerError)
	}
	defer db.Close()

	var newTeachers []models.Teacher

	// need to pass in pointed value
	err = json.NewDecoder(r.Body).Decode(&newTeachers)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
	}

	//addedTeachers := make([]models.Teacher, len(newTeachers))

	// for i, newTeacher := range newTeachers {
	// 	newTeacher.ID = nextID
	// 	teachers[nextID] = newTeacher
	// 	addedTeachers[i] = newTeacher
	// 	nextID++
	// }
	//prepare statement
	stmt, err := db.Prepare("INSERT INTO teachers (first_name, last_name , email , class , subject) VALUES (?,?,?,?,?)")

	if err != nil {
		http.Error(w, "Error preparing SQL", http.StatusInternalServerError)
	}
	defer stmt.Close()

	addedTeachers := make([]models.Teacher, len(newTeachers))

	for i, newTeacher := range newTeachers {
		res, err := stmt.Exec(newTeacher.FirstName, newTeacher.LastName, newTeacher.Email, newTeacher.Class, newTeacher.Subject)
		if err != nil {
			http.Error(w, "Error inserting daa into database", http.StatusInternalServerError)
			return
		}
		//lastinsertid and rows affected are available
		lastID, err := res.LastInsertId()
		if err != nil {
			http.Error(w, "error getting last id", http.StatusInternalServerError)
			return
		}
		newTeacher.ID = int(lastID)
		addedTeachers[i] = newTeacher
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)

	// can immediately intiailize the struct right after declaring it as one off ops
	response := struct {
		Status string           `json:"status"`
		Count  int              `json:"count"`
		Data   []models.Teacher `json:"data"`
	}{
		Status: "success",
		Count:  len(addedTeachers),
		Data:   addedTeachers,
	}
	json.NewEncoder(w).Encode(response)
}
