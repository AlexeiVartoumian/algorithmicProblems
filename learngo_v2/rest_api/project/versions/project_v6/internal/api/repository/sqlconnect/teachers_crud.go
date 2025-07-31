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

func GetTeachersDbHandler(teachers []models.Teacher, r *http.Request) ([]models.Teacher, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "Error connecting to database")
	}
	defer db.Close()

	query := "SELECT id , first_name , last_name, email , class , subject FROM teachers WHERE 1=1"
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

	//teacherList := make([]models.Teacher, 0)
	for rows.Next() {
		var teacher models.Teacher
		err := rows.Scan(&teacher.ID, &teacher.FirstName, &teacher.LastName, &teacher.Email, &teacher.Class, &teacher.Subject)

		if err != nil {
			//http.Error(w, "error scanning db results", http.StatusInternalServerError)
			return nil, utils.ErrorHandler(err, "Db scanning error")
		}
		teachers = append(teachers, teacher)

	}
	return teachers, nil
}

func GetTeacherById(id int) (models.Teacher, error) {
	db, err := ConnectDb()
	if err != nil {

		return models.Teacher{}, utils.ErrorHandler(err, "err conneciting to db")
	}
	defer db.Close()

	var teacher models.Teacher

	//query row will yield a result where scan accepts variadic parameters
	err = db.QueryRow("SELECT id , first_name , last_name ,email, class , subject FROM teachers WHERE id = ?", id).Scan(&teacher.ID, &teacher.FirstName,
		&teacher.LastName, &teacher.Email, &teacher.Class, &teacher.Subject)

	if err == sql.ErrNoRows {

		return models.Teacher{}, utils.ErrorHandler(err, "teacher no doung")
	} else if err != nil {

		return models.Teacher{}, utils.ErrorHandler(err, "Db query error")
	}
	return teacher, err
}

func AddTeachersDBHandler(newTeachers []models.Teacher) ([]models.Teacher, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "Db conn error")
	}
	defer db.Close()
	//stmt, err := db.Prepare("INSERT INTO teachers (first_name, last_name , email , class , subject) VALUES (?,?,?,?,?)")
	stmt, err := db.Prepare(utils.GenerateInsertQuery("teachers", models.Teacher{}))
	if err != nil {
		return nil, utils.ErrorHandler(err, "SQL prep statement err")
	}
	defer stmt.Close()

	addedTeachers := make([]models.Teacher, len(newTeachers))

	for i, newTeacher := range newTeachers {
		//right now these are manual need to be automated
		//res, err := stmt.Exec(newTeacher.FirstName, newTeacher.LastName, newTeacher.Email, newTeacher.Class, newTeacher.Subject)
		values := utils.GetStructValues(newTeacher)
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
		newTeacher.ID = int(lastID)
		addedTeachers[i] = newTeacher
	}
	return addedTeachers, nil
}

func UpdateTeacher(id int, updatedTeacher models.Teacher) (models.Teacher, error) {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)
		//http.Error(w, "unable to connect to database", http.StatusInternalServerError)
		return models.Teacher{}, utils.ErrorHandler(err, "Db conn error")
	}
	defer db.Close()
	var existingTeacher models.Teacher
	err = db.QueryRow("SELECT id, first_name, last_name , email , class , subject FROM teachers WHERE id = ?", id).Scan(&existingTeacher.ID,
		&existingTeacher.FirstName, &existingTeacher.LastName,
		&existingTeacher.Email, &existingTeacher.Class, &existingTeacher.Subject)

	if err != nil {
		if err == sql.ErrNoRows {
			//http.Error(w, "Teacher not found", http.StatusNotFound)
			return models.Teacher{}, utils.ErrorHandler(err, "Db query  Teacher not founderror")
		}
		//http.Error(w, "unable to retrieve data", http.StatusInternalServerError)
		return models.Teacher{}, err
	}
	updatedTeacher.ID = existingTeacher.ID
	_, err = db.Exec("UPDATE teachers SET first_name = ?, last_name = ? , email = ? , class = ? , subject = ? WHERE id = ?",
		updatedTeacher.FirstName, updatedTeacher.LastName, updatedTeacher.Email, updatedTeacher.Class, updatedTeacher.Subject,
		updatedTeacher.ID)

	if err != nil {
		//http.Error(w, " error updating teacher ", http.StatusInternalServerError)
		return models.Teacher{}, utils.ErrorHandler(err, "Db query Teacher update error")
	}
	return updatedTeacher, nil
}

func PatchTeachers(updates []map[string]interface{}) error {
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

			return utils.ErrorHandler(err, "Db query Teacher update")
		}
		id, err := strconv.Atoi(idStr)
		if err != nil {

			return utils.ErrorHandler(err, "Db query error converting id to int error")
		}

		var teacherFromDb models.Teacher
		err = db.QueryRow("SELECT id, first_name, last_name , email , class , subject FROM teachers WHERE id = ?", id).Scan(&teacherFromDb.ID,
			&teacherFromDb.FirstName, &teacherFromDb.LastName,
			&teacherFromDb.Email, &teacherFromDb.Class, &teacherFromDb.Subject)

		if err != nil {
			tx.Rollback()
			if err == sql.ErrNoRows {

				return utils.ErrorHandler(err, "Db query Teacher not found error")
			}

			return utils.ErrorHandler(err, "Error retrieveing teacher")
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
							return err
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

			return utils.ErrorHandler(err, "error updating teacher")
		}
	}
	// commit the transaction
	err = tx.Commit()
	if err != nil {

		utils.ErrorHandler(err, "Error Commiting transaction on db ")
	}
	return nil
}

func PatchOneTeacher(id int, updates map[string]interface{}) (models.Teacher, error) {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)

		return models.Teacher{}, utils.ErrorHandler(err, "Error connecting to db ")
	}
	defer db.Close()

	var existingTeacher models.Teacher
	err = db.QueryRow("SELECT id, first_name, last_name , email , class , subject FROM teachers WHERE id = ?", id).Scan(&existingTeacher.ID,
		&existingTeacher.FirstName, &existingTeacher.LastName,
		&existingTeacher.Email, &existingTeacher.Class, &existingTeacher.Subject)

	if err != nil {
		if err == sql.ErrNoRows {

			return models.Teacher{}, utils.ErrorHandler(err, "teacher not found ")
		}

		return models.Teacher{

			// rest api because of so many types may need reflection to determin the type can use reflection
		}, utils.ErrorHandler(err, "unable to retrieve data from db ")
	}

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

		return models.Teacher{}, utils.ErrorHandler(err, "error updating teacher ")
	}
	return existingTeacher, nil
}

func DeleteOneTeacher(id int) error {
	db, err := ConnectDb()
	if err != nil {
		log.Println(err)

		return utils.ErrorHandler(err, "unable to connect db ")
	}
	defer db.Close()

	result, err := db.Exec("DELETE FROM teachers WHERE id = ?", id)
	if err != nil {

		return utils.ErrorHandler(err, "unable to delete teacher db ")
	}

	//fmt.Println(result.RowsAffected())
	rowsAffected, err := result.RowsAffected()
	if err != nil {

		return utils.ErrorHandler(err, "Error retrieving delete result")
	}
	if rowsAffected == 0 {

		return utils.ErrorHandler(err, "teacher not found")
	}
	return nil
}

func DeleteTeachers(ids []int) ([]int, error) {
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
	stmt, err := tx.Prepare("DELETE FROM teachers WHERE id = ?")

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
			//http.Error(w, "Error deleting teacher", http.StatusInternalServerError)
			return nil, utils.ErrorHandler(err, "error deleteing teacher")
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

func GetStudentsByTeachersIdFromDb(teacherId string, students []models.Student) ([]models.Student, error) {
	db, err := ConnectDb()
	if err != nil {

		return nil, utils.ErrorHandler(err, "error connecting to db ")
	}
	defer db.Close()
	//if to explicaitly writing a query to retrueve student along with teacher info then could use a JOIN operation
	query := `SELECT id, first_name, last_name, email, class FROM students WHERE class = (SELECT class from teachers WHERE id = ?)`
	rows, err := db.Query(query, teacherId)
	if err != nil {
		return nil, utils.ErrorHandler(err, "error retrieveing data ")
	}
	defer rows.Close()

	for rows.Next() {
		var student models.Student
		err := rows.Scan(&student.ID, &student.FirstName, &student.LastName, &student.Email, &student.Class)
		if err != nil {
			return nil, utils.ErrorHandler(err, "error scanning rows from  db ")
		}
		students = append(students, student)
	}
	err = rows.Err()
	if err != nil {
		log.Println(err)
		return nil, utils.ErrorHandler(err, "some error wtih db.rows() ")
	}
	return students, nil
}

func GetStudentCountByTeacherIdFromDb(teacherId string) (int, error) {
	db, err := ConnectDb()
	if err != nil {

		return 0, utils.ErrorHandler(err, "error concenting to db ")
	}
	defer db.Close()

	query := `SELECT COUNT(*) FROM students WHERE class = (SELECT class FROM teachers WHERE id = ?)`

	var studentCount int
	err = db.QueryRow(query, teacherId).Scan(&studentCount)

	if err != nil {
		return 0, utils.ErrorHandler(err, "error getting data from db ")
	}
	return studentCount, nil
}
