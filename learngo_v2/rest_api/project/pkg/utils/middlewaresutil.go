// middleware is a function that wraps an http.handler with additional functionality

package utils

import "net/http"

type Middleware func(http.Handler) http.Handler

func ApplyMiddlewares(handler http.Handler, middlewares ...Middleware) http.Handler {

	for _, middleware := range middlewares {
		handler = middleware(handler)
	}
	return handler
}
