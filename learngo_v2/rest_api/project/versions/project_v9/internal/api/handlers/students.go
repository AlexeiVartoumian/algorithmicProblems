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
)

// get method old way
func GetStudentsHandler(w http.ResponseWriter, r *http.Request) {

	var Students []models.Student
	//url?limit=50&page=1
	//db will leave not show specified entreis from the beginning
	page, limit := getPaginationParams(r)
	// can immediately intiailize the struct right after declaring it as one off ops
	students, totalStudents, err := sqlconnect.GetStudentsDbHandler(Students, r, page, limit)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	response := struct {
		Status   string           `json:"status"`
		Count    int              `json:"count"`
		Page     int              `json:"page"`
		PageSize int              `json:"page_size"`
		Data     []models.Student `json:"data"`
	}{
		Status:   "success",
		Count:    totalStudents,
		Page:     page,
		PageSize: limit,
		Data:     students,
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)

}

func getPaginationParams(r *http.Request) (int, int) {

	page, err := strconv.Atoi(r.URL.Query().Get("page"))
	if err != nil {
		page = 1
	}
	limit, err := strconv.Atoi(r.URL.Query().Get("limit"))
	if err != nil {
		limit = 10
	}

	return page, limit
}

func GetOneStudentHandler(w http.ResponseWriter, r *http.Request) {

	//using golang 1.22 v extracting handler {id}
	idStr := r.PathValue("id")

	id, err := strconv.Atoi(idStr) //atio -> alphabet to intger takes string and converts to ingeger
	if err != nil {
		fmt.Println(err)
		return
	}

	//TODO will refactor for errror handiling
	Student, err := sqlconnect.GetStudentById(id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-type", "application/json")

	json.NewEncoder(w).Encode(Student)
}

// post operation get incoming request part of request body
func AddStudentHandler(w http.ResponseWriter, r *http.Request) {
	// mutex.Lock()
	// defer mutex.Unlock()

	var newStudents []models.Student
	var rawStudents []map[string]interface{}

	//request body becomes empty once used
	body, err := io.ReadAll(r.Body)
	// need to pass in pointed value
	//err := json.NewDecoder(r.Body).Decode(&newStudents)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	//err = json.NewDecoder(r.Body).Decode(&rawStudents)
	err = json.Unmarshal(body, &rawStudents)

	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
	}

	fields := GetFieldNames(models.Student{})

	allowedFields := make(map[string]struct{})
	for _, field := range fields {
		allowedFields[field] = struct{}{}
	}

	for _, Student := range rawStudents {
		for key := range Student {
			_, ok := allowedFields[key]
			if !ok {
				http.Error(w, "Unaccpetable field found in request. onl use allowed fields", http.StatusBadRequest)
				return
			}
		}
	}
	err = json.Unmarshal(body, &newStudents)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
		return
	}

	//adding data validation
	for _, Student := range newStudents {
		// if Student.FirstName == "" || Student.LastName == "" || Student.Email == "" || Student.Class == "" || Student.Subject == "" {
		// 	http.Error(w, "All fields are required", http.StatusBadRequest)
		// 	return
		// }
		err := CheckBlankFields(Student)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
	}

	addedStudents, err := sqlconnect.AddStudentsDBHandler(newStudents)
	if err != nil {

		//err.Error() is being sources from the utility func used by addStudentsdnhandler
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)

	// can immediately intiailize the struct right after declaring it as one off ops
	response := struct {
		Status string           `json:"status"`
		Count  int              `json:"count"`
		Data   []models.Student `json:"data"`
	}{
		Status: "success",
		Count:  len(addedStudents),
		Data:   addedStudents,
	}
	json.NewEncoder(w).Encode(response)
}

// Put /Students
func UpdateStudentHandler(w http.ResponseWriter, r *http.Request) {

	idStr := r.PathValue("id")
	id, err := strconv.Atoi(idStr)

	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid id", http.StatusBadRequest)
		return
	}

	var updatedStudent models.Student
	err = json.NewDecoder(r.Body).Decode(&updatedStudent)
	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid request payload", http.StatusInternalServerError)
	}

	updatedStudentFromDb, err := sqlconnect.UpdateStudent(id, updatedStudent)
	if err != nil {

		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(updatedStudentFromDb)

}

// patch /Students/
func PatchStudentsHandler(w http.ResponseWriter, r *http.Request) {

	// a list of map key val = string : interface
	var updates []map[string]interface{}
	err := json.NewDecoder(r.Body).Decode(&updates)

	if err != nil {
		http.Error(w, "invalid request Payload", http.StatusBadRequest)
		return
	}
	err = sqlconnect.PatchStudents(updates)
	if err != nil {
		log.Println(err)
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusNoContent)
}

// patch /Students/{id]}
func PatchOneStudentHandler(w http.ResponseWriter, r *http.Request) {

	idStr := strings.TrimPrefix(r.URL.Path, "/Students/")
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

	existingStudent, err := sqlconnect.PatchOneStudent(id, updates)
	if err != nil {

		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(existingStudent)

}

func DeleteOneStudentHandler(w http.ResponseWriter, r *http.Request) {

	idStr := r.PathValue("id")

	id, err := strconv.Atoi(idStr)

	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid id", http.StatusBadRequest)
		return
	}

	err = sqlconnect.DeleteOneStudent(id)
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
		Status: "Student successfully deleted",
		ID:     id,
	}
	json.NewEncoder(w).Encode(response)
}

func DeleteStudentHandler(w http.ResponseWriter, r *http.Request) {

	//extract multiple ids
	var ids []int
	err := json.NewDecoder(r.Body).Decode(&ids)
	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid request payload", http.StatusBadRequest)
		return
	}
	deletedIds, err := sqlconnect.DeleteStudents(ids)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")

	response := struct {
		Status     string `json:"status"`
		DeletedIDs []int  `json:"deleted_ids"`
	}{
		Status:     "Students successfully deleted",
		DeletedIDs: deletedIds,
	}
	json.NewEncoder(w).Encode(response)
}
