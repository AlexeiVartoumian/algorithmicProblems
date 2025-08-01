package handlers

import (
	"errors"
	"fmt"
	"reflect"
	"restapi/pkg/utils"
	"strings"
)

func CheckBlankFields(teacher interface{}) error {
	val := reflect.ValueOf(teacher)
	for i := 0; i < val.NumField(); i++ {
		field := val.Field(i)
		if field.Kind() == reflect.String && field.String() == "" {
			fmt.Println("field.Kind():", field.Kind())
			fmt.Println("reflect.String():", reflect.String)
			fmt.Println("field.String()", field.String())

			return utils.ErrorHandler(errors.New("all fields are requires"), "all fields are required")
		}
	}
	return nil
}

func GetFieldNames(model interface{}) []string {
	val := reflect.TypeOf(model)
	fields := []string{}

	for i := 0; i < val.NumField(); i++ {
		field := val.Field(i)
		fieldToAdd := strings.TrimSuffix(field.Tag.Get("json"), ",omitempty")
		fields = append(fields, fieldToAdd) //get json tag
	}
	return fields
}
