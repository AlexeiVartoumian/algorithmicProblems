package chance

import "math/rand"

// // RollADie returns a random int d with 1 <= d <= 20.
// func RollADie() int {
// 	panic("Please implement the RollADie function")
// }
func RollADie() int {
	return rand.Intn(20) + 1
}

// // GenerateWandEnergy returns a random float64 f with 0.0 <= f < 12.0.
// func GenerateWandEnergy() float64 {
// 	panic("Please implement the GenerateWandEnergy function")
// }
func GenerateWandEnergy() float64 {
	return rand.Float64() * float64(12)
}

// // ShuffleAnimals returns a slice with all eight animal strings in random order.
// func ShuffleAnimals() []string {
// 	panic("Please implement the ShuffleAnimals function")
// }

func ShuffleAnimals() []string {
	animals := []string{"ant", "beaver", "cat", "dog", "elephant", "fox", "giraffe", "hedgehog"}

	rand.Shuffle(len(animals), func(i, j int) {
		animals[i], animals[j] = animals[j], animals[i]
	})
	return animals
}
