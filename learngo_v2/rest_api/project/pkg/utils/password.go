package utils

import (
	"crypto/subtle"
	"encoding/base64"
	"errors"
	"strings"

	"golang.org/x/crypto/argon2"
)

func VerifyPassword(password, encodedHash string) error {
	parts := strings.Split(encodedHash, ".")

	if len(parts) != 2 {
		return ErrorHandler(errors.New("invalid encoded hash format"), "INternal server error")

	}
	saltBase64 := parts[0]
	hashedPasswordBase64 := parts[1]
	//then decode the base64 format
	salt, err := base64.StdEncoding.DecodeString(saltBase64)

	if err != nil {
		return ErrorHandler(err, "internal server error")

	}

	hashedPassword, err := base64.StdEncoding.DecodeString(hashedPasswordBase64)

	if err != nil {
		return ErrorHandler(err, "internal error")

	}

	//compare this hash to the one stored in the db
	hash := argon2.IDKey([]byte(password), salt, 1, 64*1024, 4, 32)

	//compare length of hash as first check
	if len(hash) != len(hashedPassword) {
		return ErrorHandler(errors.New("hash length mismatch"), "incorrect password")

	}
	// second round of comparing hash
	if subtle.ConstantTimeCompare(hash, hashedPassword) == 1 {
		//do nothing
		return nil
	} else {
		return ErrorHandler(errors.New("incorrect password"), "incorrect password")
	}

}
