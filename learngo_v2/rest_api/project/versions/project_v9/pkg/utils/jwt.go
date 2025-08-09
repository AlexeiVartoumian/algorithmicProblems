package utils

import (
	"os"
	"restapi/versions/project_v6/pkg/utils"
	"time"

	"github.com/golang-jwt/jwt/v5"
)

func SignToken(userId int, username, role string) (string, error) {
	jwtSecret := os.Getenv("JWT_SECRET")
	jwtExpiresIn := os.Getenv("JWT_EXPIRES_IN")

	//jwt contains claims docs explain flow
	claims := jwt.MapClaims{
		"uid":  userId,
		"user": username,
		"role": role,
	}
	if jwtExpiresIn == "" {
		duration, err := time.ParseDuration(jwtExpiresIn)
		if err != nil {
			return "", utils.ErrorHandler(err, "Internal error")
		}
		claims["exp"] = jwt.NewNumericDate(time.Now().Add(duration))
	} else {
		claims["exp"] = jwt.NewNumericDate(time.Now().Add(15 * time.Minute))
	}

	//not signed token
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

	signedToken, err := token.SignedString([]byte(jwtSecret))
	if err != nil {
		//zero value for strins if blan
		return "", ErrorHandler(err, "Internal error")
	}
	return signedToken, nil
}
