package logs

import (
	"strings"
	"unicode/utf8"
)

// Application identifies the application emitting the given log.
func Application(log string) string {

	for _, char := range log {
		switch int(char) {
		case 0x2757:
			return "recommendation"
		case 0x1F50D:
			return "search"
		case 0x2600:
			return "weather"
		}
	}
	return "default"
}

// Replace replaces all occurrences of old with new, returning the modified log
// to the caller.
func Replace(log string, oldRune, newRune rune) string {

	var val strings.Builder
	for _, v := range log {
		if int(v) == int(oldRune) {
			// need to encode the int32 rune into string
			val.WriteString(string(newRune))
		} else {
			val.WriteString(string(v))
		}

	}

	return val.String()
}

// WithinLimit determines whether or not the number of characters in log is
// within the limit.
func WithinLimit(log string, limit int) bool {
	return utf8.RuneCountInString(log) <= limit
}
