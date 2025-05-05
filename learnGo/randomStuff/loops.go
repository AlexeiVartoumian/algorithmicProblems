package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {

	var count int
	for i := 0; i < len(birdsPerDay); i++ {
		count += birdsPerDay[i]
	}
	return count
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	var count int
	for i := (week * 7) - 7; i < (week*7) && i < len(birdsPerDay); i++ {
		count += birdsPerDay[i]
	}
	return count
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
// func FixBirdCountLog(birdsPerDay []int) []int {
// 	panic("Please implement the FixBirdCountLog() function")
// }

func FixBirdCountLog(birdsPerDay []int) []int {

	for i := 0; i < len(birdsPerDay); i += 2 {
		birdsPerDay[i] += 1
	}
	return birdsPerDay
}
