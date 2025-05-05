package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
// func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
// 	panic("CalculateWorkingCarsPerHour not implemented")
// }

func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {

	return (float64(productionRate) / float64(100)) * successRate
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// // produced by the assembly line every minute.
// func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
// 	panic("CalculateWorkingCarsPerMinute not implemented")
// }
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {

	return int((float64(productionRate) * (successRate / float64(100))) / 60)
}

// CalculateCost works out the cost of producing the given number of cars.
// func CalculateCost(carsCount int) uint {
// 	panic("CalculateCost not implemented")
// }

func CalculateCost(carsCount int) uint {

	var mod = uint(0)
	if carsCount >= 10 {
		mod = uint((carsCount / 10) * 5000)
	}

	var total = uint(carsCount) * uint(10000)

	return total - mod

}
