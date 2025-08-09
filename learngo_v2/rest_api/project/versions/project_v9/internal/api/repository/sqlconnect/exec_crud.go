package sqlconnect

import (
	"crypto/rand"
	"crypto/sha256"
	"database/sql"
	"encoding/hex"
	"fmt"
	"log"
	"net/http"
	"os"
	"reflect"
	"restapi/models"
	"restapi/pkg/utils"
	"strconv"
	"time"

	"github.com/go-mail/mail/v2"
)

func GetExecsDbHandler(Execs []models.Exec, r *http.Request) ([]models.Exec, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "Error connecting to database")
	}
	defer db.Close()

	query := "SELECT id , first_name , last_name, email , username, user_created_at , inactive_status, role FROM Execs WHERE 1=1"
	var args []interface{}

	query, args = utils.AddFilters(r, query, args)

	query = utils.AddSorting(r, query)

	//query accepts a variadic number of argimets i.e only get by id , or by id, first_name=andy&class=Geography and so on
	rows, err := db.Query(query, args...)

	if err != nil {
		fmt.Println(err)

		return nil, utils.ErrorHandler(err, "Db query error")
	}
	defer rows.Close()

	//ExecList := make([]models.Exec, 0)
	for rows.Next() {
		var Exec models.Exec
		err := rows.Scan(&Exec.ID, &Exec.FirstName, &Exec.LastName, &Exec.Email, &Exec.UserName, &Exec.UserCreatedAt,
			&Exec.InactiveStatus, &Exec.Role)

		if err != nil {
			//http.Error(w, "error scanning db results", http.StatusInternalServerError)
			return nil, utils.ErrorHandler(err, "Db scanning error")
		}
		Execs = append(Execs, Exec)

	}
	return Execs, nil
}

func GetExecById(id int) (models.Exec, error) {
	db, err := ConnectDb()
	if err != nil {

		return models.Exec{}, utils.ErrorHandler(err, "err conneciting to db")
	}
	defer db.Close()

	var Exec models.Exec

	//query row will yield a result where scan accepts variadic parameters
	err = db.QueryRow("SELECT id , first_name , last_name ,email, username , inactive_status,role FROM Execs WHERE id = ?", id).Scan(&Exec.ID, &Exec.FirstName,
		&Exec.LastName, &Exec.Email, &Exec.UserName, &Exec.InactiveStatus, &Exec.Role)

	if err == sql.ErrNoRows {

		return models.Exec{}, utils.ErrorHandler(err, "Exec no doung")
	} else if err != nil {

		return models.Exec{}, utils.ErrorHandler(err, "Db query error")
	}
	return Exec, err
}

func AddExecsDBHandler(newExecs []models.Exec) ([]models.Exec, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "Db conn error")
	}
	defer db.Close()
	//stmt, err := db.Prepare("INSERT INTO Execs (first_name, last_name , email , class , subject) VALUES (?,?,?,?,?)")
	stmt, err := db.Prepare(utils.GenerateInsertQuery("Execs", models.Exec{}))
	if err != nil {

		return nil, utils.ErrorHandler(err, "SQL prep statement err")
	}
	defer stmt.Close()

	addedExecs := make([]models.Exec, len(newExecs))

	for i, newExec := range newExecs {
		//right now these are manual need to be automated
		//res, err := stmt.Exec(newExec.FirstName, newExec.LastName, newExec.Email, newExec.Class, newExec.Subject)

		newExec.Password, err = utils.HashPassword(newExec.Password)
		if err != nil {
			return nil, utils.ErrorHandler(err, "error adding exec into database")
		}

		values := utils.GetStructValues(newExec)
		fmt.Println("output of func", values)
		res, err := stmt.Exec(values...)
		if err != nil {

			return nil, utils.ErrorHandler(err, "Db insertion error")
		}
		//lastinsertid and rows affected are available
		lastID, err := res.LastInsertId()
		if err != nil {
			//http.Error(w, "error getting last id", http.StatusInternalServerError)
			return nil, utils.ErrorHandler(err, "err getting last id")
		}
		newExec.ID = int(lastID)
		addedExecs[i] = newExec
	}
	return addedExecs, nil
}

func PatchExecs(updates []map[string]interface{}) error {
	db, err := ConnectDb()
	if err != nil {
		return utils.ErrorHandler(err, "error updating data")
	}
	defer db.Close()

	tx, err := db.Begin()
	if err != nil {
		return utils.ErrorHandler(err, "error updating data")
	}

	for _, update := range updates {
		idStr, ok := update["id"].(string)
		if !ok {
			tx.Rollback()
			return utils.ErrorHandler(err, "invalid Id")
		}

		id, err := strconv.Atoi(idStr)
		if err != nil {
			tx.Rollback()
			return utils.ErrorHandler(err, "invalid Id")
		}

		var ExecFromDb models.Exec
		err = db.QueryRow("SELECT id, first_name, last_name, email, username FROM execs WHERE id = ?", id).Scan(&ExecFromDb.ID, &ExecFromDb.FirstName, &ExecFromDb.LastName, &ExecFromDb.Email, &ExecFromDb.UserName)
		if err != nil {
			tx.Rollback()
			if err == sql.ErrNoRows {
				return utils.ErrorHandler(err, "Exec not found")
			}
			return utils.ErrorHandler(err, "error updating data")
		}

		execVal := reflect.ValueOf(&ExecFromDb).Elem()
		execType := execVal.Type()

		for k, v := range update {
			if k == "id" {
				continue // skip updating the ID field
			}
			for i := 0; i < execVal.NumField(); i++ {
				field := execType.Field(i)
				if field.Tag.Get("json") == k+",omitempty" {
					fieldVal := execVal.Field(i)
					if fieldVal.CanSet() {
						val := reflect.ValueOf(v)
						if val.Type().ConvertibleTo(fieldVal.Type()) {
							fieldVal.Set(val.Convert(fieldVal.Type()))
						} else {
							tx.Rollback()
							log.Printf("cannot convert %v to %v", val.Type(), fieldVal.Type())
							return utils.ErrorHandler(err, "error updating data")
						}
					}
					break
				}
			}
		}

		_, err = tx.Exec("UPDATE execs SET first_name = ?, last_name = ?, email = ?, username = ? WHERE id = ?", ExecFromDb.FirstName, ExecFromDb.LastName, ExecFromDb.Email, ExecFromDb.UserName, ExecFromDb.ID)
		if err != nil {
			tx.Rollback()
			return utils.ErrorHandler(err, "error updating data")
		}
	}

	err = tx.Commit()
	if err != nil {
		return utils.ErrorHandler(err, "error updating data")
	}
	return nil
}

func PatchOneExec(id int, updates map[string]interface{}) (models.Exec, error) {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)
		return models.Exec{}, utils.ErrorHandler(err, "error updating data")
	}
	defer db.Close()

	var existingExec models.Exec
	err = db.QueryRow("SELECT id, first_name, last_name, email, username FROM execs WHERE id = ?", id).Scan(&existingExec.ID, &existingExec.FirstName,
		&existingExec.LastName, &existingExec.Email, &existingExec.UserName)
	if err != nil {
		if err == sql.ErrNoRows {
			return models.Exec{}, utils.ErrorHandler(err, "Exec not found")
		}
		return models.Exec{}, utils.ErrorHandler(err, "error updating data")
	}

	execVal := reflect.ValueOf(&existingExec).Elem()
	execType := execVal.Type()

	for k, v := range updates {
		for i := 0; i < execVal.NumField(); i++ {
			field := execType.Field(i)
			if field.Tag.Get("json") == k+",omitempty" {
				if execVal.Field(i).CanSet() {
					fieldVal := execVal.Field(i)
					fieldVal.Set(reflect.ValueOf(v).Convert(execVal.Field(i).Type()))
				}
			}
		}
	}

	_, err = db.Exec("UPDATE execs SET first_name = ?, last_name = ?, email = ?, username = ? WHERE id = ?", existingExec.FirstName, existingExec.LastName, existingExec.Email, &existingExec.UserName, existingExec.ID)
	if err != nil {
		return models.Exec{}, utils.ErrorHandler(err, "error updating data")
	}
	return existingExec, nil
}

func DeleteOneExec(id int) error {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)

		return utils.ErrorHandler(err, "unable to connect db ")
	}
	defer db.Close()

	result, err := db.Exec("DELETE FROM Execs WHERE id = ?", id)
	if err != nil {

		return utils.ErrorHandler(err, "unable to delete Exec db ")
	}

	//fmt.Println(result.RowsAffected())
	rowsAffected, err := result.RowsAffected()
	if err != nil {

		return utils.ErrorHandler(err, "Error retrieving delete result")
	}
	if rowsAffected == 0 {

		return utils.ErrorHandler(err, "Exec not found")
	}
	return nil
}

func GetUserByUserName(username string) (*models.Exec, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "err conneciting to db")

	}
	defer db.Close()

	//query and scan into a user stuct
	user := &models.Exec{}
	err = db.QueryRow(`SELECT id , first_name, last_name , email , username, password , inactive_status , role FROM execs WHERE username = ?`, username).Scan(&user.ID, &user.FirstName,
		&user.LastName, &user.Email, &user.UserName, &user.Password, &user.InactiveStatus, &user.Role)

	if err != nil {
		if err == sql.ErrNoRows {
			return nil, utils.ErrorHandler(err, "user not found ")
		}

		return nil, utils.ErrorHandler(err, "db error")
	}
	return user, nil
}

func UpdatePasswordInDb(userId int, currentPassword, newPassword string) (bool, error) {
	db, err := ConnectDb()
	if err != nil {
		return false, utils.ErrorHandler(err, "database connection error")
	}
	defer db.Close()

	var username string
	var userPassword string
	var userRole string

	err = db.QueryRow("SELECT username , password , role FROM execs WHERE id = ?", userId).Scan(&username, &userPassword, &userRole)

	if err != nil {

		return false, utils.ErrorHandler(err, "user not found")
	}

	err = utils.VerifyPassword(currentPassword, userPassword)
	if err != nil {

		return false, utils.ErrorHandler(err, "the password you enterd does not match the current one")
	}

	hashedPassword, err := utils.HashPassword(newPassword)
	if err != nil {

		return false, utils.ErrorHandler(err, "internal error")
	}
	currentTime := time.Now().Format(time.RFC3339)

	_, err = db.Exec("UPDATE execs SET password = ? , password_changed_at = ? WHERE id = ?", hashedPassword, currentTime, userId)
	if err != nil {
		return false, utils.ErrorHandler(err, "failed to update the password")

	}

	// token, err := utils.SignToken(userId, username, userRole)
	// if err != nil {
	// 	utils.ErrorHandler(err, "passwrod updated could not create token ")
	// }
	// return hashedPassword
	return true, nil

}

func ForgeotPasswordDbHandler(emailId string) error {
	db, err := ConnectDb()
	if err != nil {

		return utils.ErrorHandler(err, "Internal error")
	}
	defer db.Close()

	var exec models.Exec
	err = db.QueryRow("SELECT id FROM execs WHERE email = ?", emailId).Scan(&exec.ID)
	if err != nil {

		return utils.ErrorHandler(err, "User not found")
	}
	duration, err := strconv.Atoi(os.Getenv("RESET_TOKEN_EXP_DURATION"))
	if err != nil {

		return utils.ErrorHandler(err, "Failed to send password reset email")
	}
	mins := time.Duration(duration)
	expiry := time.Now().Add(mins * time.Minute).Format(time.RFC3339)

	//created empty byteslice
	tokenBytes := make([]byte, 32)
	//read random bytes into the slice
	_, err = rand.Read(tokenBytes)

	if err != nil {
		utils.ErrorHandler(err, "Failed to send password reset email")
		return utils.ErrorHandler(err, "Failed to send password reset email")
	}
	log.Println("tokenBytes", tokenBytes)
	//then encodoed to string
	token := hex.EncodeToString(tokenBytes)
	log.Println("token", token)
	//then hashed the token string two differnet values from same source token and hashedtoken
	hashedToken := sha256.Sum256(tokenBytes)
	log.Println("hashedToken", hashedToken)

	hashedTokenString := hex.EncodeToString(hashedToken[:])

	_, err = db.Exec("UPDATE execs SET password_reset_token = ?, password_token_expires = ? WHERE id = ?", hashedTokenString, expiry, exec.ID)
	if err != nil {
		utils.ErrorHandler(err, "Failed to send password reset eamil ")
	}

	//once live becomes domain for reset email
	resetUrl := fmt.Sprintf("https://localhost:3000/execs/resetpassword/reset/%s", token)
	message := fmt.Sprintf("Forgot your password? Reset your password using the following link: \n%s\nIf you didnt request a password reset please ignore this email. this link is only valid for %d minustes.", resetUrl, int(mins))

	m := mail.NewMessage()
	m.SetHeader("From", "schooladmin@school.com")
	m.SetHeader("To", emailId)
	m.SetHeader("Subject", "Your password reset link")
	m.SetBody("text/plain", message)

	mail.NewDialer("localhost", 1025, "", "")

	d := mail.NewDialer("localhost", 1025, "", "")

	err = d.DialAndSend(m)
	if err != nil {
		return utils.ErrorHandler(err, "Failed to send password rest email")

	}
	return nil
}

func ResetPasswordDbHandler(hashedTokenstring string, newPassword string) error {
	db, err := ConnectDb()
	if err != nil {

		return utils.ErrorHandler(err, "Internal error")

	}
	defer db.Close()

	var user models.Exec

	//decoding token string into byte slice
	bytes, err := hex.DecodeString(hashedTokenstring)

	if err != nil {
		return utils.ErrorHandler(err, "internal error")

	}
	hashedToken := sha256.Sum256(bytes)
	hashedTokenString := hex.EncodeToString(hashedToken[:])

	query := "SELECT id, email FROM execs WHERE password_reset_token = ? AND password_token_expires > ?"
	err = db.QueryRow(query, hashedTokenString, time.Now().Format(time.RFC3339)).Scan(&user.ID, &user.Email)

	if err != nil {
		return utils.ErrorHandler(err, "invalid or expired reset code ")

	}
	hashedPassword, err := utils.HashPassword(newPassword)
	if err != nil {
		return utils.ErrorHandler(err, "internal error")

	}
	updatedQuery := "UPDATE execs SET password = ?, password_reset_token = NULL, password_token_expires = NULL, password_changed_at = ? WHERE id = ?"
	_, err = db.Exec(updatedQuery, hashedPassword, time.Now().Format(time.RFC3339), user.ID)

	if err != nil {
		return utils.ErrorHandler(err, "Internal error")

	}
	return nil
}
