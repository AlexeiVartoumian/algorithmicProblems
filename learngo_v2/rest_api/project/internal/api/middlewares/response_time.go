package middlewares

import (
	"fmt"
	"net/http"
	"time"
)

// TODO refactor the wau time is being logged
func ResponseTimeMiddleware(next http.Handler) http.Handler {

	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("Recieved Reqiest in response time")
		start := time.Now()

		//create a custom ResponseWriter to capture the status code
		wrappedWriter := &responseWriter{ResponseWriter: w, status: http.StatusOK}

		//calculate duration
		duration := time.Since(start)
		wrappedWriter.Header().Set("X-Response-Time", duration.String())
		next.ServeHTTP(wrappedWriter, r)

		duration = time.Since(start)
		//finally log the req details
		fmt.Printf("Method: %s , URL: %s , Status %d Duration %v\n", r.Method, r.URL, wrappedWriter.status, duration.String())
		fmt.Println("Sent repsonse from response writer")
	})
}

// responseWriter , chuck in response times can do this because this is an http repsonse writer is interface
// recall that embedded methods on the interface/strcut are accessible to outer structs as well
type responseWriter struct {
	http.ResponseWriter
	status int
}

func (rw *responseWriter) WriteHeader(code int) {
	rw.status = code
	rw.ResponseWriter.WriteHeader(code)
}
