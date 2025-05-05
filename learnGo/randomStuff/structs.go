package speed

// TODO: define the 'Car' type struct

// NewCar creates a new remote controlled car with full battery and given specifications.
// func NewCar(speed, batteryDrain int) Car {
// 	panic("Please implement the NewCar function")
// }
type Car struct {
    battery int
    batteryDrain int
    speed int
    distance int
}

func NewCar( speed int , batteryDrain int ) Car {

    return Car {
        battery: 100,
        speed:  speed,
        batteryDrain:  batteryDrain,
    }
}
    

// TODO: define the 'Track' type struct
type Track struct {
    distance int
}
// NewTrack creates a new track
// func NewTrack(distance int) Track {
// 	panic("Please implement the NewTrack function")
// }
func NewTrack(distance int) Track {
    return Track{
        distance : distance,
    }
}

// Drive drives the car one time. If there is not enough battery to drive one more time,
// the car will not move.
// func Drive(car Car) Car {
// 	panic("Please implement the Drive function")
// }
func Drive(car Car) Car {
    if car.battery - car.batteryDrain >= 0 {
        car.battery -= car.batteryDrain
    	car.distance += car.speed
        return car
    }else{
        return car
    }
    
}

// CanFinish checks if a car is able to finish a certain track.
func CanFinish(car Car, track Track) bool {

    return float32(track.distance / car.speed ) * float32(car.batteryDrain) <= float32(car.battery) 
}
