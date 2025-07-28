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
	"strings"
)

func GetStudentsDbHandler(Students []models.Student, r *http.Request) ([]models.Student, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "Error connecting to database")
	}
	defer db.Close()

	query := "SELECT id , first_name , last_name, email , class FROM Students WHERE 1=1"
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

	//StudentList := make([]models.Student, 0)
	for rows.Next() {
		var Student models.Student
		err := rows.Scan(&Student.ID, &Student.FirstName, &Student.LastName, &Student.Email, &Student.Class)

		if err != nil {
			//http.Error(w, "error scanning db results", http.StatusInternalServerError)
			return nil, utils.ErrorHandler(err, "Db scanning error")
		}
		Students = append(Students, Student)

	}
	return Students, nil
}

func GetStudentById(id int) (models.Student, error) {
	db, err := ConnectDb()
	if err != nil {

		return models.Student{}, utils.ErrorHandler(err, "err conneciting to db")
	}
	defer db.Close()

	var Student models.Student

	//query row will yield a result where scan accepts variadic parameters
	err = db.QueryRow("SELECT id , first_name , last_name ,email, class FROM Students WHERE id = ?", id).Scan(&Student.ID, &Student.FirstName,
		&Student.LastName, &Student.Email, &Student.Class)

	if err == sql.ErrNoRows {

		return models.Student{}, utils.ErrorHandler(err, "Student no doung")
	} else if err != nil {

		return models.Student{}, utils.ErrorHandler(err, "Db query error")
	}
	return Student, err
}

func AddStudentsDBHandler(newStudents []models.Student) ([]models.Student, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "Db conn error")
	}
	defer db.Close()
	//stmt, err := db.Prepare("INSERT INTO Students (first_name, last_name , email , class , subject) VALUES (?,?,?,?,?)")
	stmt, err := db.Prepare(utils.GenerateInsertQuery("Students", models.Student{}))
	if err != nil {

		return nil, utils.ErrorHandler(err, "SQL prep statement err")
	}
	defer stmt.Close()

	addedStudents := make([]models.Student, len(newStudents))

	for i, newStudent := range newStudents {
		//right now these are manual need to be automated
		//res, err := stmt.Exec(newStudent.FirstName, newStudent.LastName, newStudent.Email, newStudent.Class, newStudent.Subject)
		values := utils.GetStructValues(newStudent)
		fmt.Println("output of func", values)
		res, err := stmt.Exec(values...)
		if err != nil {
			fmt.Println("------Error-------", err.Error())
			if strings.Contains(err.Error(), "a foreign key constraint fails (`school`.`students`, CONSTRAINT `students_ibfk_1` FOREIGN KEY (`class`) REFERENCES `teachers` (`class`))") {
				return nil, utils.ErrorHandler(err, "class input on student does not have a teacher class t reference")
			}
			return nil, utils.ErrorHandler(err, "Db insertion error")
		}
		//lastinsertid and rows affected are available
		lastID, err := res.LastInsertId()
		if err != nil {
			//http.Error(w, "error getting last id", http.StatusInternalServerError)
			return nil, utils.ErrorHandler(err, "err getting last id")
		}
		newStudent.ID = int(lastID)
		addedStudents[i] = newStudent
	}
	return addedStudents, nil
}

func UpdateStudent(id int, updatedStudent models.Student) (models.Student, error) {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)
		//http.Error(w, "unable to connect to database", http.StatusInternalServerError)
		return models.Student{}, utils.ErrorHandler(err, "Db conn error")
	}
	defer db.Close()
	var existingStudent models.Student
	err = db.QueryRow("SELECT id, first_name, last_name , email , class FROM Students WHERE id = ?", id).Scan(&existingStudent.ID,
		&existingStudent.FirstName, &existingStudent.LastName,
		&existingStudent.Email, &existingStudent.Class)

	if err != nil {
		if err == sql.ErrNoRows {
			//http.Error(w, "Student not found", http.StatusNotFound)
			return models.Student{}, utils.ErrorHandler(err, "Db query  Student not founderror")
		}
		//http.Error(w, "unable to retrieve data", http.StatusInternalServerError)
		return models.Student{}, err
	}
	updatedStudent.ID = existingStudent.ID
	_, err = db.Exec("UPDATE Students SET first_name = ?, last_name = ? , email = ? , class = ? WHERE id = ?",
		updatedStudent.FirstName, updatedStudent.LastName, updatedStudent.Email, updatedStudent.Class,
		updatedStudent.ID)

	if err != nil {
		//http.Error(w, " error updating Student ", http.StatusInternalServerError)
		return models.Student{}, utils.ErrorHandler(err, "Db query Student update error")
	}
	return updatedStudent, nil
}

func PatchStudents(updates []map[string]interface{}) error {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)

		return utils.ErrorHandler(err, "Db conn error")
	}
	defer db.Close()
	tx, err := db.Begin()

	if err != nil {
		log.Println(err)

		return utils.ErrorHandler(err, "Db query transaction")
	}

	for _, update := range updates {
		idStr, ok := update["id"].(string)
		if !ok {
			tx.Rollback()

			return utils.ErrorHandler(err, "Db query Student update")
		}
		id, err := strconv.Atoi(idStr)
		if err != nil {

			return utils.ErrorHandler(err, "Db query error converting id to int error")
		}

		var StudentFromDb models.Student
		err = db.QueryRow("SELECT id, first_name, last_name , email , class FROM Students WHERE id = ?", id).Scan(&StudentFromDb.ID,
			&StudentFromDb.FirstName, &StudentFromDb.LastName,
			&StudentFromDb.Email, &StudentFromDb.Class)

		if err != nil {
			tx.Rollback()
			if err == sql.ErrNoRows {

				return utils.ErrorHandler(err, "Db query Student not found error")
			}

			return utils.ErrorHandler(err, "Error retrieveing Student")
		}

		//apply updates using reflection
		StudentVal := reflect.ValueOf(&StudentFromDb).Elem()
		StudentType := StudentVal.Type()

		for k, v := range update {
			if k == "id" {
				continue // skip updating id field
			}
			for i := 0; i < StudentVal.NumField(); i++ {
				field := StudentType.Field(i)
				if field.Tag.Get("json") == k+",omitempty" {
					fieldVal := StudentVal.Field(i)
					if fieldVal.CanSet() {
						val := reflect.ValueOf(v)
						if val.Type().ConvertibleTo(fieldVal.Type()) {
							fieldVal.Set(val.Convert(fieldVal.Type()))
						} else {
							tx.Rollback()
							log.Printf("cannot convert %v to %v", val.Type(), fieldVal.Type())
							return err
						}
					}
					break
				}
			}
		}
		_, err = tx.Exec("UPDATE Students SET first_name = ?, last_name = ? , email = ? , class = ? WHERE id = ?",
			StudentFromDb.FirstName, StudentFromDb.LastName, StudentFromDb.Email,
			StudentFromDb.Class, StudentFromDb.ID)

		if err != nil {
			tx.Rollback()

			return utils.ErrorHandler(err, "error updating Student")
		}
	}
	// commit the transaction
	err = tx.Commit()
	if err != nil {

		utils.ErrorHandler(err, "Error Commiting transaction on db ")
	}
	return nil
}

func PatchOneStudent(id int, updates map[string]interface{}) (models.Student, error) {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)

		return models.Student{}, utils.ErrorHandler(err, "Error connecting to db ")
	}
	defer db.Close()

	var existingStudent models.Student
	err = db.QueryRow("SELECT id, first_name, last_name , email , class FROM Students WHERE id = ?", id).Scan(&existingStudent.ID,
		&existingStudent.FirstName, &existingStudent.LastName,
		&existingStudent.Email, &existingStudent.Class)

	if err != nil {
		if err == sql.ErrNoRows {

			return models.Student{}, utils.ErrorHandler(err, "Student not found ")
		}

		return models.Student{

			// rest api because of so many types may need reflection to determin the type can use reflection
		}, utils.ErrorHandler(err, "unable to retrieve data from db ")
	}

	StudentVal := reflect.ValueOf(&existingStudent).Elem()
	StudentType := StudentVal.Type()
	fmt.Println("StudentType field 0", StudentVal.Type().Field(0))
	fmt.Println("StudentType field 1", StudentVal.Type().Field(1))

	// this will handle any number of fields in a struct usin g reflect
	for k, v := range updates {
		for i := 0; i < StudentVal.NumField(); i++ {
			//fmt.Println("k from reflect meachnism", k)
			field := StudentType.Field(i)
			//fmt.Println(field.Tag.Get("json"))

			//match the key to value in json field
			if field.Tag.Get("json") == k+",omitempty" {
				if StudentVal.Field(i).CanSet() {
					fieldVal := StudentVal.Field(i)
					fmt.Println("fieldVal", fieldVal)
					fmt.Println("StudentVal.Field(i).Type()", StudentVal.Field(i).Type())
					fmt.Println("reflect.ValueOf(v) ", reflect.ValueOf(v))
					fieldVal.Set(reflect.ValueOf(v).Convert(StudentVal.Field(i).Type()))
				}
			}

		}
	}

	_, err = db.Exec("UPDATE Students SET first_name = ?, last_name = ? , email = ? , class = ? WHERE id = ?",
		existingStudent.FirstName, existingStudent.LastName, existingStudent.Email, existingStudent.Class,
		existingStudent.ID)

	if err != nil {

		return models.Student{}, utils.ErrorHandler(err, "error updating Student ")
	}
	return existingStudent, nil
}

func DeleteOneStudent(id int) error {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)

		return utils.ErrorHandler(err, "unable to connect db ")
	}
	defer db.Close()

	result, err := db.Exec("DELETE FROM Students WHERE id = ?", id)
	if err != nil {

		return utils.ErrorHandler(err, "unable to delete Student db ")
	}

	//fmt.Println(result.RowsAffected())
	rowsAffected, err := result.RowsAffected()
	if err != nil {

		return utils.ErrorHandler(err, "Error retrieving delete result")
	}
	if rowsAffected == 0 {

		return utils.ErrorHandler(err, "Student not found")
	}
	return nil
}

func DeleteStudents(ids []int) ([]int, error) {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)

		return nil, utils.ErrorHandler(err, "unable to conn to db")
	}
	defer db.Close()

	tx, err := db.Begin()
	if err != nil {
		log.Println(err)

		return nil, utils.ErrorHandler(err, "err starting transaction")

	}
	stmt, err := tx.Prepare("DELETE FROM Students WHERE id = ?")

	if err != nil {
		tx.Rollback()

		return nil, utils.ErrorHandler(err, "Error preparing delete statement")
	}
	defer stmt.Close()

	deletedIds := []int{}
	for _, id := range ids {
		result, err := stmt.Exec(id)
		if err != nil {
			tx.Rollback()
			log.Println(err)
			//http.Error(w, "Error deleting Student", http.StatusInternalServerError)
			return nil, utils.ErrorHandler(err, "error deleteing Student")
		}
		result.RowsAffected()
		//fmt.Println(result.RowsAffected())
		rowsAffected, err := result.RowsAffected()
		if err != nil {
			tx.Rollback()

			return nil, utils.ErrorHandler(err, "error retriveing delete result")
		}
		if rowsAffected > 0 {
			deletedIds = append(deletedIds, id)
		}
		if rowsAffected < 1 {
			tx.Rollback()

			return nil, utils.ErrorHandler(err, fmt.Sprintf("id %d not found", id))
		}
	}
	err = tx.Commit()
	if err != nil {
		log.Println(err)
		//http.Error(w, "Error commtting transaction", http.StatusInternalServerError)
		return nil, utils.ErrorHandler(err, "error commtting transaction to db ")
	}

	if len(deletedIds) < 1 {
		//http.Error(w, "ids do not exist", http.StatusBadRequest)
		return nil, utils.ErrorHandler(err, "id do not exist ")
	}
	return deletedIds, nil
}
