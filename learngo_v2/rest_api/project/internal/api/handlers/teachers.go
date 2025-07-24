package handlers

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"reflect"
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

func isValidSortOrder(order string) bool {
	return order == "asc" || order == "desc"
}
func isValidSortField(field string) bool {
	validFields := map[string]bool{
		"first_name": true,
		"last_name":  true,
		"email":      true,
		"class":      true,
		"subject":    true,
	}
	return validFields[field]

}

// get method old way
func GetTeachersHandler(w http.ResponseWriter, r *http.Request) {

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		http.Error(w, "Error connecting to databae", http.StatusInternalServerError)
	}
	defer db.Close()

	// path := strings.TrimPrefix(r.URL.Path, "/teachers/")
	// idStr := strings.TrimSuffix(path, "/")
	// fmt.Println(idStr)

	teacherList := make([]models.Teacher, 0)

	//handle multple gets on db query
	//if sure to get one result then use db.Queryrow else use db.Query for multiple results
	query := "SELECT id , first_name , last_name, email , class , subject FROM teachers WHERE 1=1"
	var args []interface{}

	query, args = addFilters(r, query, args)

	query = addSorting(r, query)

	//query accepts a variadic number of argimets i.e only get by id , or by id, first_name=andy&class=Geography and so on
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

func GetOneTeacherHandler(w http.ResponseWriter, r *http.Request) {

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		http.Error(w, "Error connecting to databae", http.StatusInternalServerError)
	}
	defer db.Close()

	//using golang 1.22 v extracting handler {id}
	idStr := r.PathValue("id")

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

func addSorting(r *http.Request, query string) string {
	sortParams := r.URL.Query()["sortby"]
	// tea
	if len(sortParams) > 0 {
		query += " ORDER BY"

		for i, param := range sortParams {
			parts := strings.Split(param, ":")

			if len(parts) != 2 {
				continue
			}
			field, order := parts[0], parts[1]
			if !isValidSortField(field) || !isValidSortOrder(order) {
				continue
			}
			if i > 0 {
				query += " ,"
			}
			query += " " + field + " " + order
		}
	}
	return query
}

// construct a multi-parameter get request
func addFilters(r *http.Request, query string, args []interface{}) (string, []interface{}) {
	params := map[string]string{
		"first_name": "first_name",
		"last_name":  "last_name",
		"email":      "email",
		"class":      "class",
		"subject":    "subject",
	}
	//parse url query parameter string
	for param, dbField := range params {
		value := r.URL.Query().Get(param)
		if value != "" {
			query += " AND " + dbField + " = ?"
			args = append(args, value)
		}
	}
	return query, args
}

// post operation get incoming request part of request body
func AddTeacherHandler(w http.ResponseWriter, r *http.Request) {
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

// Put /teachers
func UpdateTeacherHandler(w http.ResponseWriter, r *http.Request) {

	idStr := r.PathValue("id")
	id, err := strconv.Atoi(idStr)

	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid id", http.StatusBadRequest)
		return
	}

	var updatedTeacher models.Teacher
	err = json.NewDecoder(r.Body).Decode(&updatedTeacher)
	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid request payload", http.StatusInternalServerError)
	}

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		log.Println(err)
		http.Error(w, "unable to connect to database", http.StatusInternalServerError)
		return
	}
	defer db.Close()
	var existingTeacher models.Teacher
	err = db.QueryRow("SELECT id, first_name, last_name , email , class , subject FROM teachers WHERE id = ?", id).Scan(&existingTeacher.ID,
		&existingTeacher.FirstName, &existingTeacher.LastName,
		&existingTeacher.Email, &existingTeacher.Class, &existingTeacher.Subject)

	if err != nil {
		if err == sql.ErrNoRows {
			http.Error(w, "Teacher not found", http.StatusNotFound)
			return
		}
		http.Error(w, "unable to retrieve data", http.StatusInternalServerError)
		return
	}
	updatedTeacher.ID = existingTeacher.ID
	_, err = db.Exec("UPDATE teachers SET first_name = ?, last_name = ? , email = ? , class = ? , subject = ? WHERE id = ?",
		updatedTeacher.FirstName, updatedTeacher.LastName, updatedTeacher.Email, updatedTeacher.Class, updatedTeacher.Subject,
		updatedTeacher.ID)

	if err != nil {
		http.Error(w, " error updating teacher ", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(updatedTeacher)

}

// patch /teachers/
func PatchTeachersHandler(w http.ResponseWriter, r *http.Request) {

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		log.Println(err)
		http.Error(w, "unable to connect to database", http.StatusInternalServerError)
		return
	}
	defer db.Close()

	// a list of map key val = string : interface
	var updates []map[string]interface{}
	err = json.NewDecoder(r.Body).Decode(&updates)

	if err != nil {
		http.Error(w, "invalid request Payload", http.StatusBadRequest)
		return
	}
	// runnning a transaction that is multiple sql statements in sequence. either all succeed or all fail
	//acid properts -> atomicty , consistency ,isolation , durability
	// atomocity = all ok or none
	// consistency = db starts in one valid state and transforms to another valid state
	// isolation = transactions are isloaled from each other
	// durability = once transation is done its permanent
	tx, err := db.Begin()

	if err != nil {
		log.Println(err)
		http.Error(w, "Error startin transaction", http.StatusBadRequest)
		return
	}

	for _, update := range updates {
		idStr, ok := update["id"].(string)
		if !ok {
			tx.Rollback()
			http.Error(w, "Invalid Teacher id in update", http.StatusBadRequest)
			return
		}
		id, err := strconv.Atoi(idStr)
		if err != nil {
			http.Error(w, "error converting id to int in update ", http.StatusBadRequest)
		}

		var teacherFromDb models.Teacher
		err = db.QueryRow("SELECT id, first_name, last_name , email , class , subject FROM teachers WHERE id = ?", id).Scan(&teacherFromDb.ID,
			&teacherFromDb.FirstName, &teacherFromDb.LastName,
			&teacherFromDb.Email, &teacherFromDb.Class, &teacherFromDb.Subject)

		if err != nil {
			tx.Rollback()
			if err == sql.ErrNoRows {
				http.Error(w, "Teacher not found", http.StatusNotFound)
				return
			}
			http.Error(w, "Error retrieveing teacher", http.StatusInternalServerError)
			return
		}

		//apply updates using reflection
		teacherVal := reflect.ValueOf(&teacherFromDb).Elem()
		teacherType := teacherVal.Type()

		for k, v := range update {
			if k == "id" {
				continue // skip updating id field
			}
			for i := 0; i < teacherVal.NumField(); i++ {
				field := teacherType.Field(i)
				if field.Tag.Get("json") == k+",omitempty" {
					fieldVal := teacherVal.Field(i)
					if fieldVal.CanSet() {
						val := reflect.ValueOf(v)
						if val.Type().ConvertibleTo(fieldVal.Type()) {
							fieldVal.Set(val.Convert(fieldVal.Type()))
						} else {
							tx.Rollback()
							log.Printf("cannot convert %v to %v", val.Type(), fieldVal.Type())
							return
						}
					}
					break
				}
			}
		}
		_, err = tx.Exec("UPDATE teachers SET first_name = ?, last_name = ? , email = ? , class = ? , subject = ? WHERE id = ?",
			teacherFromDb.FirstName, teacherFromDb.LastName, teacherFromDb.Email,
			teacherFromDb.Class, teacherFromDb.Class, teacherFromDb.ID)

		if err != nil {
			tx.Rollback()
			http.Error(w, " error updating teacher ", http.StatusInternalServerError)
			return
		}
	}
	// commit the transaction
	err = tx.Commit()
	if err != nil {
		http.Error(w, "Error Commiting transaction", http.StatusInternalServerError)
	}
	w.WriteHeader(http.StatusNoContent)
}

// patch /teachers/{id]}
func PatchOneTeachersHandler(w http.ResponseWriter, r *http.Request) {

	idStr := strings.TrimPrefix(r.URL.Path, "/teachers/")
	id, err := strconv.Atoi(idStr)

	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid id", http.StatusBadRequest)
		return
	}

	var updates map[string]interface{}
	err = json.NewDecoder(r.Body).Decode(&updates)
	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid request payload", http.StatusInternalServerError)
	}

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		log.Println(err)
		http.Error(w, "unable to connect to database", http.StatusInternalServerError)
		return
	}
	defer db.Close()

	var existingTeacher models.Teacher
	err = db.QueryRow("SELECT id, first_name, last_name , email , class , subject FROM teachers WHERE id = ?", id).Scan(&existingTeacher.ID,
		&existingTeacher.FirstName, &existingTeacher.LastName,
		&existingTeacher.Email, &existingTeacher.Class, &existingTeacher.Subject)

	if err != nil {
		if err == sql.ErrNoRows {
			http.Error(w, "Teacher not found", http.StatusNotFound)
			return
		}
		http.Error(w, "unable to retrieve data", http.StatusInternalServerError)
		return
	}

	// rest api because of so many types may need reflection to determin the type can use reflection
	teacherVal := reflect.ValueOf(&existingTeacher).Elem()
	teacherType := teacherVal.Type()
	fmt.Println("TeacherType field 0", teacherVal.Type().Field(0))
	fmt.Println("TeacherType field 1", teacherVal.Type().Field(1))

	// this will handle any number of fields in a struct usin g reflect
	for k, v := range updates {
		for i := 0; i < teacherVal.NumField(); i++ {
			//fmt.Println("k from reflect meachnism", k)
			field := teacherType.Field(i)
			//fmt.Println(field.Tag.Get("json"))

			//match the key to value in json field
			if field.Tag.Get("json") == k+",omitempty" {
				if teacherVal.Field(i).CanSet() {
					fieldVal := teacherVal.Field(i)
					fmt.Println("fieldVal", fieldVal)
					fmt.Println("teacherVal.Field(i).Type()", teacherVal.Field(i).Type())
					fmt.Println("reflect.ValueOf(v) ", reflect.ValueOf(v))
					fieldVal.Set(reflect.ValueOf(v).Convert(teacherVal.Field(i).Type()))
				}
			}

		}
	}

	_, err = db.Exec("UPDATE teachers SET first_name = ?, last_name = ? , email = ? , class = ? , subject = ? WHERE id = ?",
		existingTeacher.FirstName, existingTeacher.LastName, existingTeacher.Email, existingTeacher.Class, existingTeacher.Subject,
		existingTeacher.ID)

	if err != nil {
		http.Error(w, " error updating teacher ", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(existingTeacher)

}

func DeleteOneTeacherHandler(w http.ResponseWriter, r *http.Request) {

	idStr := r.PathValue("id")

	id, err := strconv.Atoi(idStr)

	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid id", http.StatusBadRequest)
		return
	}

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		log.Println(err)
		http.Error(w, "unable to connect to database", http.StatusInternalServerError)
		return
	}
	defer db.Close()

	result, err := db.Exec("DELETE FROM teachers WHERE id = ?", id)
	if err != nil {
		http.Error(w, "Error deleteing teacher", http.StatusInternalServerError)
		return
	}

	//fmt.Println(result.RowsAffected())
	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, "Error retrieving delete result", http.StatusInternalServerError)
		return
	}
	if rowsAffected == 0 {
		http.Error(w, "Teahcer not found", http.StatusNotFound)
		return
	}
	//w.WriteHeader(http.StatusNoContent)

	w.Header().Set("Content-Type", "application/json")
	response := struct {
		Status string `json:"status"`
		ID     int    `json:"id"`
	}{
		Status: "Teacher successfully deleted",
		ID:     id,
	}
	json.NewEncoder(w).Encode(response)
}

func DeleteTeacherHandler(w http.ResponseWriter, r *http.Request) {

	db, err := sqlconnect.ConnectDb()
	if err != nil {
		log.Println(err)
		http.Error(w, "unable to connect to database", http.StatusInternalServerError)
		return
	}
	defer db.Close()

	//extract multiple ids
	var ids []int
	err = json.NewDecoder(r.Body).Decode(&ids)
	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid request payload", http.StatusBadRequest)
		return
	}

	tx, err := db.Begin()
	if err != nil {
		log.Println(err)
		http.Error(w, "error starting transaction", http.StatusBadRequest)
		return

	}
	stmt, err := tx.Prepare("DELETE FROM teachers WHERE id = ?")

	if err != nil {
		tx.Rollback()
		http.Error(w, "Error perparing delete statametnr teacher", http.StatusInternalServerError)
		return
	}
	defer stmt.Close()

	deletedIds := []int{}
	for _, id := range ids {
		result, err := stmt.Exec(id)
		if err != nil {
			tx.Rollback()
			log.Println(err)
			http.Error(w, "Error deleting teacher", http.StatusInternalServerError)
			return
		}
		result.RowsAffected()
		//fmt.Println(result.RowsAffected())
		rowsAffected, err := result.RowsAffected()
		if err != nil {
			tx.Rollback()
			http.Error(w, "Error retireving delete result", http.StatusInternalServerError)
		}
		if rowsAffected > 0 {
			deletedIds = append(deletedIds, id)
		}
		if rowsAffected < 1 {
			tx.Rollback()
			http.Error(w, fmt.Sprintf("ID %d does not exist", id), http.StatusInternalServerError)
			return
		}
	}
	err = tx.Commit()
	if err != nil {
		log.Println(err)
		http.Error(w, "Error commtting transaction", http.StatusInternalServerError)
		return
	}

	if len(deletedIds) < 1 {
		http.Error(w, "ids do not exist", http.StatusBadRequest)
		return
	}

	w.Header().Set("Content-Type", "application/json")

	response := struct {
		Status     string `json:"status"`
		DeletedIDs []int  `json:"deleted_ids"`
	}{
		Status:     "Teachers successfully deleted",
		DeletedIDs: deletedIds,
	}
	json.NewEncoder(w).Encode(response)
}
