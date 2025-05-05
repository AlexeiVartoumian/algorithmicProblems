package electionday

import "fmt"

// NewVoteCounter returns a new vote counter with
// a given number of initial votes.
// func NewVoteCounter(initialVotes int) *int {

// }
func NewVoteCounter(initialVotes int) *int {

	var countInMemory *int
	countInMemory = &initialVotes // countinMemory is not the reference to passed in variable

	return countInMemory
}

// VoteCount extracts the number of votes from a counter.
// func VoteCount(counter *int) int {
// 	panic("Please implement the VoteCount() function")
// }
func VoteCount(counter *int) int {
	if counter != nil {
		return *counter
	}
	return 0
}

// // IncrementVoteCount increments the value in a vote counter.
// func IncrementVoteCount(counter *int, increment int) {
// 	panic("Please implement the IncrementVoteCount() function")
// }
func IncrementVoteCount(counter *int, increment int) {

	*counter += increment
}

// // NewElectionResult creates a new election result.
// func NewElectionResult(candidateName string, votes int) *ElectionResult {
// 	panic("Please implement the NewElectionResult() function")
// }
func NewElectionResult(candidateName string, votes int) *ElectionResult {

	return &ElectionResult{Name: candidateName, Votes: votes}
}

// DisplayResult creates a message with the result to be displayed.
// func DisplayResult(result *ElectionResult) string {
// 	panic("Please implement the DisplayResult() function")
// }
func DisplayResult(result *ElectionResult) string {

	return fmt.Sprintf("%s (%d)", result.Name, result.Votes)
}

// DecrementVotesOfCandidate decrements by one the vote count of a candidate in a map.
// func DecrementVotesOfCandidate(results map[string]int, candidate string) {
// 	panic("Please implement the DecrementVotesOfCandidate() function")
// }
func DecrementVotesOfCandidate(results map[string]int, candidate string) {
	results[candidate] -= 1
}
