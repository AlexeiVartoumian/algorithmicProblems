package middlewares

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"restapi/versions/project_v5/pkg/utils"
	"strings"

	"github.com/microcosm-cc/bluemonday"
)

// middlewares here a re filtering the request
func XSSMiddleware(next http.Handler) http.Handler {
	fmt.Println("***** Initializing XSSMiddleware")
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

		fmt.Println("++++++++ XSSMiddleware ran")
		//sanitize the url path
		sanitizedPath, err := clean(r.URL.Path)
		if err != nil {
			http.Error(w, "invalid path", http.StatusBadRequest)
			return
		}
		fmt.Println("Original path:", r.URL.Path)
		fmt.Println("Sanitized path", sanitizedPath)

		//sanitize query params
		params := r.URL.Query()
		sanitizedQuery := make(map[string][]string)

		for key, values := range params {
			sanitizedKey, err := clean(key)
			if err != nil {
				http.Error(w, err.Error(), http.StatusBadRequest)
				return
			}

			var sanitizedValues []string
			for _, value := range values {
				cleanValue, err := clean(value)
				if err != nil {
					http.Error(w, err.Error(), http.StatusBadRequest)
					return
				}
				//since cleanvalue is of type interface convert to string
				sanitizedValues = append(sanitizedValues, cleanValue.(string))
			}
			sanitizedQuery[sanitizedKey.(string)] = sanitizedValues
			fmt.Println("Original query %s: %s \n", key, strings.Join(values, " "))
			fmt.Println("Sanitized Query %s: %s\n", sanitizedKey, strings.Join(sanitizedValues, ", "))
		}

		r.URL.Path = sanitizedPath.(string)
		r.URL.RawQuery = url.Values(sanitizedQuery).Encode()
		fmt.Println("UPdates url", r.URL.String())

		//sanitze request body
		if r.Header.Get("Content-Type") == "application/json" {
			if r.Body != nil {
				//need to read the request body
				bodyBytes, err := io.ReadAll(r.Body)
				if err != nil {
					http.Error(w, "error reading request body", http.StatusBadRequest)
					return
				}

				bodyString := strings.TrimSpace(string(bodyBytes))
				fmt.Println("Original Body:", bodyString)
				// reset the request body
				r.Body = io.NopCloser(bytes.NewReader([]byte(bodyString)))

				if len(bodyString) > 0 {
					var inputData interface{}
					err := json.NewDecoder(bytes.NewReader([]byte(bodyString))).Decode(&inputData)

					if err != nil {
						http.Error(w, utils.ErrorHandler(err, "Invalid json body").Error(), http.StatusBadRequest)
						return
					}
					fmt.Println("Original JSON data", inputData)
					sanitizedData, err := clean(inputData)
					if err != nil {
						http.Error(w, err.Error(), http.StatusBadRequest)
						return
					}

					fmt.Println("Sanitized JSON data", sanitizedData)

					//MARHSAL THE SANIZTED DATA BACK TO THE BODY
					sanitizedBody, err := json.Marshal(sanitizedData)
					if err != nil {
						http.Error(w, utils.ErrorHandler(err, "Error Sanitizing body").Error(), http.StatusBadRequest)
					}
					// now that we have santizied marhsle body now need to store into request and override intitali requrest
					r.Body = io.NopCloser(bytes.NewReader(sanitizedBody))
					fmt.Println("Sanitized body", string(sanitizedBody))
				} else {
					fmt.Println("Requst body is empty")
				}
			} else {
				log.Println("No body in the request")
			}
		} else if r.Header.Get("Content-Type") != "" {
			log.Printf("Received request with unsupported Content-Type: %s . Expected application/json", r.Header.Get("Content-Type"))
			http.Error(w, "Unsupported Content-Type . please use applicaiton/json", http.StatusUnsupportedMediaType)
		}

		next.ServeHTTP(w, r)
		fmt.Println("Sending response from XSSMIddleware ran ")
	})
}

// clean sanitizes input data to prevent xss attacks where data can be represented in below data formats
func clean(data interface{}) (interface{}, error) {

	//here v not only carries the type but also the data
	switch v := data.(type) {

	case map[string]interface{}:
		for key, value := range v {
			v[key] = sanitizeValue(value)
		}
		return v, nil
	case []interface{}:
		for i, value := range v {
			v[i] = sanitizeValue(value)
		}
		return sanitizeValue(v), nil
	case string:
		return sanitizeString(v), nil
	default:

		return nil, utils.ErrorHandler(fmt.Errorf("unsupported typ: %T", data), fmt.Sprintf("unsupported type %T", data))
	}

}

func sanitizeValue(data interface{}) interface{} {

	switch v := data.(type) {
	case string:
		return sanitizeString(v)
	case map[string]interface{}:
		for k, value := range v {
			v[k] = sanitizeValue(value)
		}
		return v
	case []interface{}:
		for i, value := range v {
			v[i] = sanitizeValue(value)
		}
	default:
		return v
	}
	return nil

}

func sanitizeString(value string) string {

	//bluemonday is a library where underneath the hood is applying a bunch of
	//regexes to sanitize
	return bluemonday.UGCPolicy().Sanitize(value)
}
