package techpalace

import (
	"strings"
	"unicode"
)

// WelcomeMessage returns a welcome message for the customer.
// func WelcomeMessage(customer string) string {
// 	//panic("Please implement the WelcomeMessage() function")
// }

func WelcomeMessage(customer string) string {
	var welcomeMessage = "Welcome to the Tech Palace, "
	return welcomeMessage + strings.ToUpper(customer)
}

// AddBorder adds a border to a welcome message.
// func AddBorder(welcomeMsg string, numStarsPerLine int) string {
// 	panic("Please implement the AddBorder() function")
// }

func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	var stars = strings.Repeat("*", numStarsPerLine)
	return stars + "\n" + welcomeMsg + "\n" + stars
}

// CleanupMessage cleans up an old marketing message.
//
//	func CleanupMessage(oldMsg string) string {
//		panic("Please implement the CleanupMessage() function")
//	}
func CleanupMessage(oldMsg string) string {

	return strings.TrimFunc(oldMsg, func(r rune) bool {
		return !(unicode.IsLetter(r) || !unicode.IsNumber(r) || r == '%')
	})
}
