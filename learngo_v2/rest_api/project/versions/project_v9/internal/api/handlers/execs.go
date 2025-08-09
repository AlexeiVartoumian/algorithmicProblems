package handlers

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"restapi/internal/api/repository/sqlconnect"
	"restapi/models"
	"restapi/pkg/utils"
	"strconv"
	"strings"
	"time"
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

func LoginHandler(w http.ResponseWriter, r *http.Request) {
	var req models.Exec
	// data validation
	err := json.NewDecoder(r.Body).Decode(&req)

	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
	}
	defer r.Body.Close()

	if req.UserName == "" || req.Password == "" {
		http.Error(w, "Username and passowrd are required", http.StatusBadRequest)
		return
	}
	// search ofr user if exist in db

	user, err := sqlconnect.GetUserByUserName(req.UserName)
	if err != nil {
		http.Error(w, "invalid username or password", http.StatusBadRequest)
		return
	}
	//user active
	//we know stuct val is boolean
	if user.InactiveStatus {
		http.Error(w, "Account is inaceive", http.StatusBadRequest)
	}
	//verify pass retrieved from db and split by .
	err = utils.VerifyPassword(req.Password, user.Password)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	//gen jwt token
	fmt.Println(user.ID)
	fmt.Println()
	tokenString, err := utils.SignToken(user.ID, req.UserName, user.Role)
	if err != nil {
		http.Error(w, "Could not create login token", http.StatusInternalServerError)
		return
	}

	// send token as response or as cookie
	http.SetCookie(w, &http.Cookie{
		Name:     "Bearer",
		Value:    tokenString,
		Path:     "/",
		HttpOnly: true,
		Secure:   true,
		Expires:  time.Now().Add(24 * time.Hour),
		SameSite: http.SameSiteStrictMode,
	})
	//can set multiple cookie
	http.SetCookie(w, &http.Cookie{
		Name:     "test",
		Value:    "testing",
		Path:     "/",
		HttpOnly: true,
		Secure:   true,
		Expires:  time.Now().Add(24 * time.Hour),
		SameSite: http.SameSiteStrictMode,
	})
	// in practise only send jwt token as a cookie no need for header
	w.Header().Set("Content-Type", "application/json")
	response := struct {
		Token string `json:"token"`
	}{
		Token: tokenString,
	}
	json.NewEncoder(w).Encode(response)
}

func LogoutHandler(w http.ResponseWriter, r *http.Request) {
	// removing stuff from client side making sure tokens cant be used no more

	// clear jwt cookie
	http.SetCookie(w, &http.Cookie{
		Name:     "Bearer",
		Value:    "",
		Path:     "/",
		HttpOnly: true,
		Secure:   true,
		Expires:  time.Unix(0, 0),
		SameSite: http.SameSiteStrictMode,
	})
	w.Header().Set("Content-Type", "application-type/json")
	w.Write([]byte(`{"message": "Logged out successfully"}`))

	// blacklist jwt and check against middleware?
}

func UpdatePasswordHandler(w http.ResponseWriter, r *http.Request) {
	idStr := r.PathValue("id")
	userId, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "Invalid exec ID", http.StatusBadRequest)
	}

	var req models.UpdatePasswordRequest
	err = json.NewDecoder(r.Body).Decode(&req)

	if err != nil {
		http.Error(w, "invalid rquest body", http.StatusBadRequest)
	}
	r.Body.Close()

	if req.CurrentPassword == "" || req.NewPassword == "" {
		http.Error(w, "please enter password", http.StatusBadRequest)
		return
	}

	_, err = sqlconnect.UpdatePasswordInDb(userId, req.CurrentPassword, req.NewPassword)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// send token as response or as cookie
	// http.SetCookie(w, &http.Cookie{
	// 	Name:     "Bearer",
	// 	Value:    token,
	// 	Path:     "/",
	// 	HttpOnly: true,
	// 	Secure:   true,
	// 	Expires:  time.Now().Add(24 * time.Hour),
	// 	SameSite: http.SameSiteStrictMode,
	// })

	// in practise only send jwt token as a cookie no need for header
	w.Header().Set("Content-Type", "application/json")
	response := struct {
		Message string `json:"token"`
	}{
		Message: "Password updated successfully",
	}
	json.NewEncoder(w).Encode(response)
}

func ForgotPasswordHandler(w http.ResponseWriter, r *http.Request) {
	var req struct {
		Email string `json:""`
	}

	err := json.NewDecoder(r.Body).Decode(&req)
	if err != nil || req.Email == "" {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	r.Body.Close()

	err = sqlconnect.ForgeotPasswordDbHandler(req.Email)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	fmt.Fprintf(w, "password reset link to %s ", req.Email)

}

func ResetPasswordHandler(w http.ResponseWriter, r *http.Request) {
	token := r.PathValue("resetcode")

	type request struct {
		NewPassword     string `json:"new_password"`
		ConfirmPassword string `json:"confirm_password"`
	}

	var req request

	err := json.NewDecoder(r.Body).Decode(&req)

	if err != nil || req.NewPassword == "" || req.ConfirmPassword == "" {
		http.Error(w, "invalid values in request", http.StatusBadRequest)
	}

	if req.NewPassword != req.ConfirmPassword {
		http.Error(w, "passwords should match", http.StatusBadRequest)
		return
	}
	err = sqlconnect.ResetPasswordDbHandler(token, req.NewPassword)
	if err != nil {
		http.Error(w, "Passwords should match", http.StatusBadRequest)
		return
	}
	fmt.Fprintln(w, "Password reset successfully")
}
