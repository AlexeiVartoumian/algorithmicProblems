package parsinglogfiles

import (
	"regexp"
	"strings"
)

func IsValidLine(text string) bool {

	re := regexp.MustCompile(`^\[(TRC|DBG|INF|WRN|ERR|FTL)\]`)
	return re.MatchString(text)
}

func SplitLogLine(text string) []string {
	re := regexp.MustCompile(`<[-~*=]*>`)

	return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	count := 0
	quoteRe := regexp.MustCompile(`"([^"]*)"`) // match quoted text

	for _, line := range lines {
		match := quoteRe.FindStringSubmatch(line)
		if len(match) > 1 {
			quoted := strings.ToLower(match[1])
			if strings.Contains(quoted, "password") {
				count++
			}
		}
	}
	return count
}

func RemoveEndOfLineText(text string) string {

	re := regexp.MustCompile(`end-of-line\d+`)
	return re.ReplaceAllString(text, "")
}

func TagWithUserName(lines []string) []string {
	re := regexp.MustCompile(`User\s+(\S+)`)
	result := []string{}

	for _, line := range lines {
		matches := re.FindStringSubmatch(line)
		if len(matches) > 1 {
			username := matches[1]
			tagged := "[USR] " + username + " " + line
			result = append(result, tagged)
		} else {
			result = append(result, line)
		}
	}
	return result
}
