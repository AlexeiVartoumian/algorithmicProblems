package middlewares

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"restapi/pkg/utils"

	"github.com/golang-jwt/jwt/v5"
)

type ContextKey string

func JWTMiddleware(next http.Handler) http.Handler {
	fmt.Println("------------- JWT MIDDLEWARE-------------")
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		fmt.Println("+++++++ Inside")
		//fmt.Println(r.Cookie("Bearer"))

		token, err := r.Cookie("Bearer")

		if err != nil {
			http.Error(w, "authorization header missing", http.StatusUnauthorized)
			return
		}
		jwtSecret := os.Getenv("JWT_SECRET")

		//now need to validate and parse the token
		parsedToken, err := jwt.Parse(token.Value, func(token *jwt.Token) (interface{}, error) {
			//Dont forect to validate the alg is what oyu expect:

			if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
				return nil, fmt.Errorf("UNxpected sisnging method: %v", token.Header["alg"])
			}
			return []byte(jwtSecret), nil
		})
		if err != nil {
			utils.ErrorHandler(err, "")
			http.Error(w, err.Error(), http.StatusUnauthorized)
			return
		}
		if parsedToken.Valid {
			log.Println("Valid jwt")
		} else {
			log.Println("Invalid jsw", token.Value)

		}

		fmt.Println("PArsed TOken", parsedToken)
		claims, ok := parsedToken.Claims.(jwt.MapClaims)
		if !ok {
			http.Error(w, "invalid token", http.StatusUnauthorized)
			return
		}

		ctx := context.WithValue(r.Context(), ContextKey("role"), claims["role"])
		ctx = context.WithValue(ctx, ContextKey("expiresAt"), claims["exp"])
		ctx = context.WithValue(ctx, ContextKey("username"), claims["user"])
		ctx = context.WithValue(ctx, ContextKey("userId"), claims["uid"])

		fmt.Println(ctx)

		next.ServeHTTP(w, r.WithContext(ctx))
		fmt.Println("Sent resoponses frmo jwt middleware")
	})
}
