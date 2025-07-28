package middlewares

import (
	"fmt"
	"net/http"
)

// allowed origin specify who can access the resources
var allowedOrigins = []string{
	"https://my-origin.com",
	"https://localhost:3000",
}

//eg api and frontend are at two different endpoints
//api is hosted at www.myapi.com
// frontend is at some_frontend.com -> only frontend will be able to access

func Cors(next http.Handler) http.Handler {
	fmt.Println("Cors middleware...")
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Cors middleware being returned")
		//extract the header //checking the origin her
		//origin := r.Header.Get("Accept-Encoding")
		origin := r.Header.Get("Origin")
		fmt.Println(origin)

		if isOriginAllowed(origin) {
			w.Header().Set("Access-Control-Allow-Origin", origin)
		} else {
			http.Error(w, "Not allowed by Cors", http.StatusForbidden)
			return
		}

		w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT , PATCH, DELETE")
		w.Header().Set("Access-Control-Allow-Credentials", "true")
		w.Header().Set("Access-Control-Expose-Headers", "Authorization")
		w.Header().Set("Access-Control-Max-age", "3600")

		//preflight check performed by browsers no need to send response
		if r.Method == http.MethodOptions {
			return
		}

		next.ServeHTTP(w, r)
	})

}

func isOriginAllowed(origin string) bool {

	for _, allowedOrigin := range allowedOrigins {
		if origin == allowedOrigin {
			return true
		}
	}
	return false
}
