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
func GetExecsHandler(w http.ResponseWriter, r *http.Request) {

	var Execs []models.Exec
	Execs, err := sqlconnect.GetExecsDbHandler(Execs, r)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// can immediately intiailize the struct right after declaring it as one off ops
	response := struct {
		Status string        `json:"status"`
		Count  int           `json:"count"`
		Data   []models.Exec `json:"data"`
	}{
		Status: "success",
		Count:  len(Execs),
		Data:   Execs,
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)

}

func GetOneExecsHandler(w http.ResponseWriter, r *http.Request) {

	//using golang 1.22 v extracting handler {id}
	idStr := r.PathValue("id")

	id, err := strconv.Atoi(idStr) //atio -> alphabet to intger takes string and converts to ingeger
	if err != nil {
		fmt.Println(err)
		return
	}

	//TODO will refactor for errror handiling
	Exec, err := sqlconnect.GetExecById(id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-type", "application/json")

	json.NewEncoder(w).Encode(Exec)
}

// post operation get incoming request part of request body
func AddExecsHandler(w http.ResponseWriter, r *http.Request) {
	// mutex.Lock()
	// defer mutex.Unlock()

	var newExecs []models.Exec
	var rawExecs []map[string]interface{}

	//request body becomes empty once used
	body, err := io.ReadAll(r.Body)
	// need to pass in pointed value
	//err := json.NewDecoder(r.Body).Decode(&newExecs)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
		return
	}
	defer r.Body.Close()

	//err = json.NewDecoder(r.Body).Decode(&rawExecs)
	err = json.Unmarshal(body, &rawExecs)

	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
	}

	fields := GetFieldNames(models.Exec{})

	allowedFields := make(map[string]struct{})
	for _, field := range fields {
		allowedFields[field] = struct{}{}
	}

	for _, Exec := range rawExecs {
		for key := range Exec {
			_, ok := allowedFields[key]
			if !ok {
				http.Error(w, "Unaccpetable field found in request. onl use allowed fields", http.StatusBadRequest)
				return
			}
		}
	}
	err = json.Unmarshal(body, &newExecs)
	if err != nil {
		http.Error(w, "INvalid Request Body", http.StatusBadRequest)
		return
	}

	//adding data validation
	for _, Exec := range newExecs {
		// if Exec.FirstName == "" || Exec.LastName == "" || Exec.Email == "" || Exec.Class == "" || Exec.Subject == "" {
		// 	http.Error(w, "All fields are required", http.StatusBadRequest)
		// 	return
		// }
		err := CheckBlankFields(Exec)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
	}

	addedExecs, err := sqlconnect.AddExecsDBHandler(newExecs)
	if err != nil {

		//err.Error() is being sources from the utility func used by addExecsdnhandler
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)

	// can immediately intiailize the struct right after declaring it as one off ops
	response := struct {
		Status string        `json:"status"`
		Count  int           `json:"count"`
		Data   []models.Exec `json:"data"`
	}{
		Status: "success",
		Count:  len(addedExecs),
		Data:   addedExecs,
	}
	json.NewEncoder(w).Encode(response)
}

// patch /Execs/
func PatchExecsHandler(w http.ResponseWriter, r *http.Request) {

	// a list of map key val = string : interface
	var updates []map[string]interface{}
	err := json.NewDecoder(r.Body).Decode(&updates)

	if err != nil {
		http.Error(w, "invalid request Payload", http.StatusBadRequest)
		return
	}
	err = sqlconnect.PatchExecs(updates)
	if err != nil {
		log.Println(err)
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusNoContent)
}

// patch /Execs/{id]}
func PatchOneExecHandler(w http.ResponseWriter, r *http.Request) {

	idStr := strings.TrimPrefix(r.URL.Path, "/execs/")
	id, err := strconv.Atoi(idStr)

	if err != nil {

		http.Error(w, "Invalid id", http.StatusBadRequest)
		return
	}

	var updates map[string]interface{}
	err = json.NewDecoder(r.Body).Decode(&updates)
	if err != nil {
		log.Println(err)
		http.Error(w, "invalid request payload", http.StatusBadRequest)
	}

	existingExec, err := sqlconnect.PatchOneExec(id, updates)
	if err != nil {

		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(existingExec)

}

func DeleteOneExecHandler(w http.ResponseWriter, r *http.Request) {

	idStr := r.PathValue("id")

	id, err := strconv.Atoi(idStr)

	if err != nil {
		log.Println(err)
		http.Error(w, "Invalid id", http.StatusBadRequest)
		return
	}

	err = sqlconnect.DeleteOneExec(id)
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
		Status: "Exec successfully deleted",
		ID:     id,
	}
	json.NewEncoder(w).Encode(response)
}
