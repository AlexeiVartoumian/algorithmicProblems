package sqlconnect

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"reflect"
	"restapi/models"
	"restapi/pkg/utils"
	"strconv"
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
