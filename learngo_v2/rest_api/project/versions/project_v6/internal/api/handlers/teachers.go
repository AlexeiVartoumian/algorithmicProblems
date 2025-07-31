package handlers

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
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

// get method old way
func GetTeachersHandler(w http.ResponseWriter, r *http.Request) {

	var teachers []models.Teacher
	teachers, err := sqlconnect.GetTeachersDbHandler(teachers, r)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// can immediately intiailize the struct right after declaring it as one off ops
	response := struct {
		Status string           `json:"status"`
		Count  int              `json:"count"`
		Data   []models.Teacher `json:"data"`
	}{
		Status: "success",
		Count:  len(teachers),
		Data:   teachers,
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)

}

func GetOneTeacherHandler(w http.ResponseWriter, r *http.Request) {

	//using golang 1.22 v extracting handler {id}
	idStr := r.PathValue("id")

	id, err := strconv.Atoi(idStr) //atio -> alphabet to intger takes string and converts to ingeger
	if err != nil {
		fmt.Println(err)
		return
	}

	//TODO will refactor for errror handiling
	teacher, err := sqlconnect.GetTeacherById(id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-type", "application/json")

	json.NewEncoder(w).Encode(teacher)
}

// post operation get incoming request part of request body
func AddTeacherHandler(w http.ResponseWriter, r *http.Request) {
	// mutex.Lock()
	// defer mutex.Unlock()

	var newTeachers []models.Teacher
	var rawTeachers []map[string]interface{}

	//request body becomes empty once used
	body, err := io.ReadAll(r.Body)
	// need to pass in pointed value
	//err := json.NewDecoder(r.Body).Decode(&newTeachers)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	//err = json.NewDecoder(r.Body).Decode(&rawTeachers)
	err = json.Unmarshal(body, &rawTeachers)

	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
	}

	fields := GetFieldNames(models.Teacher{})

	allowedFields := make(map[string]struct{})
	for _, field := range fields {
		allowedFields[field] = struct{}{}
	}

	for _, teacher := range rawTeachers {
		for key := range teacher {
			_, ok := allowedFields[key]
			if !ok {
				http.Error(w, "Unaccpetable field found in request. onl use allowed fields", http.StatusBadRequest)
				return
			}
		}
	}
	err = json.Unmarshal(body, &newTeachers)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
		return
	}

	//adding data validation
	for _, teacher := range newTeachers {
		// if teacher.FirstName == "" || teacher.LastName == "" || teacher.Email == "" || teacher.Class == "" || teacher.Subject == "" {
		// 	http.Error(w, "All fields are required", http.StatusBadRequest)
		// 	return
		// }
		err := CheckBlankFields(teacher)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
	}

	addedTeachers, err := sqlconnect.AddTeachersDBHandler(newTeachers)
	if err != nil {

		//err.Error() is being sources from the utility func used by addteachersdnhandler
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
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

	updatedTeacherFromDb, err := sqlconnect.UpdateTeacher(id, updatedTeacher)
	if err != nil {

		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(updatedTeacherFromDb)

}

// patch /teachers/
func PatchTeachersHandler(w http.ResponseWriter, r *http.Request) {

	// a list of map key val = string : interface
	var updates []map[string]interface{}
	err := json.NewDecoder(r.Body).Decode(&updates)

	if err != nil {
		http.Error(w, "invalid request Payload", http.StatusBadRequest)
		return
	}
	err = sqlconnect.PatchTeachers(updates)
	if err != nil {
		log.Println(err)
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
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

	existingTeacher, err := sqlconnect.PatchOneTeacher(id, updates)
	if err != nil {

		http.Error(w, err.Error(), http.StatusInternalServerError)
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

	err = sqlconnect.DeleteOneTeacher(id)
	if err != nil {

		http.Error(w, err.Error(), http.StatusInternalServerError)
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

	//extract multiple ids
	var ids []int
	err := json.NewDecoder(r.Body).Decode(&ids)
	if err != nil {
		http.Error(w, "Invalid request payload", http.StatusBadRequest)
		return
	}
	deletedIds, err := sqlconnect.DeleteTeachers(ids)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
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

// subroutes functionality cross reference /locate students based on teacher class
func GetStudentsByTeachersId(w http.ResponseWriter, r *http.Request) {

	teacherId := r.PathValue("id")

	var students []models.Student

	students, err := sqlconnect.GetStudentsByTeachersIdFromDb(teacherId, students)
	if err != nil {
		http.Error(w, "Invalid request payload", http.StatusBadRequest)
		return
	}
	//can immediately create
	response := struct {
		Status string           `json:"status"`
		Count  int              `json:"count"`
		Data   []models.Student `json:"data"`
	}{
		Status: "success",
		Count:  len(students),
		Data:   students,
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func GetStudentCountByTeacherId(w http.ResponseWriter, r *http.Request) {

	teacherId := r.PathValue("id")

	var studentCount int

	studentCount, err := sqlconnect.GetStudentCountByTeacherIdFromDb(teacherId)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	response := struct {
		Status string `json:"status"`
		Count  int    `json:"count"`
	}{
		Status: "success",
		Count:  studentCount,
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)

}
