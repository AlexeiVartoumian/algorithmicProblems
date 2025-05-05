package purchase

import (
	"math"
)

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {

	if kind == "car" || kind == "truck" {
		return true
	}
	return false
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in lexicographical order.
func ChooseVehicle(option1, option2 string) string {

	var val1 byte
	var val2 byte
	var smaller = math.Min(float64(len(option1)), float64(len(option2)))
	var sm string
	if len(option1) < len(option2) {
		smaller = float64(len(option1))
		sm = option1
	} else {
		smaller = float64(len(option2))
		sm = option2
	}

	for i := 0; i < int(smaller); i++ {
		val1, val2 = option1[i], option2[i]

		if val1 < val2 {
			return option1 + " is clearly the better choice."
		} else if val2 < val1 {
			return option2 + " is clearly the better choice."
		}
	}
	return sm + " is clearly the better choice."

}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice, age float64) float64 {

	if age >= 10 {
		return originalPrice / 2
	} else if age >= 3 {

		return originalPrice * 0.7
	} else {
		return originalPrice * 0.8
	}

}
