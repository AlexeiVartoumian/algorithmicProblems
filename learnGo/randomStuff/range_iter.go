package chessboard

// Declare a type named File which stores if a square is occupied by a piece - this will be a slice of bools

type File []bool

// Declare a type named Chessboard which contains a map of eight Files, accessed with keys from "A" to "H"
type Chessboard map[string]File

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file.
func CountInFile(cb Chessboard, file string) int {

	val, exists := cb[file]
	if !exists {
		return 0
	}
	var count = 0
	for _, v := range val {
		if v {
			count++
		}
	}
	return count
}

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank.
func CountInRank(cb Chessboard, rank int) int {

	if rank > 8 || rank < 1 {
		return 0
	}
	var count = 0
	for k := range cb {
		if cb[k][rank-1] {
			count++
		}
	}
	return count
}

// CountAll should count how many squares are present in the chessboard.
func CountAll(cb Chessboard) int {
	return 64
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) int {

	var squares = 0

	for _, v := range cb {

		for _, value := range v {
			if value {
				squares++
			}
		}
	}
	return squares
}
