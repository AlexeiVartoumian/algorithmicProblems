Introduction
Stringer is an interface for defining the string format of values.

The interface consists of a single String method:

type Stringer interface {
    String() string
}
Types that want to implement this interface must have a String() method that returns a human-friendly string representation of the type. The fmt package (and many others) will look for this method to format and print values.

Example: Distances
Assume we are working on an application that deals with geographical distances measured in different units. We have defined types DistanceUnit and Distance as follows:

type DistanceUnit int

const (
	Kilometer    DistanceUnit = 0
	Mile         DistanceUnit = 1
)
 
type Distance struct {
	number float64
	unit   DistanceUnit
} 
In the example above, Kilometer and Mile are constants of type DistanceUnit.

These types do not implement interface Stringer as they lack the String method. Hence fmt functions will print Distance values using Go's "default format":

mileUnit := Mile
fmt.Sprint(mileUnit)
// => 1
// The result is '1' because that is the underlying value of the 'Mile' constant (see constant declarations above) 

dist := Distance{number: 790.7, unit: Kilometer}
fmt.Sprint(dist)
// => {790.7 0}
// not a very useful output!
In order to make the output more informative, we implement interface Stringer for DistanceUnit and Distance types by adding a String method to each type:

func (sc DistanceUnit) String() string {
	units := []string{"km", "mi"}
	return units[sc]
}

func (d Distance) String() string {
	return fmt.Sprintf("%v %v", d.number, d.unit)
}
fmt package functions will call these methods when formatting Distance values:

kmUnit := Kilometer
kmUnit.String()
// => km

mileUnit := Mile
mileUnit.String()
// => mi

dist := Distance{
	number: 790.7,
	unit: Kilometer,
}
dist.String()
// => 790.7 km
Instructions
Your team is working on a meteorology application. They have defined an API with various types and constants representing meteorological data, see file meteorology.go.

Your task is to add suitable String methods to all types so that they implement interface Stringer.

After some discussion, the team have agreed that the unit of temperature will be either Celsius or Fahrenheit. Values should be formatted as shown in the examples below.

Make the TemperatureUnit type implement the Stringer interface by adding a String method to it. This method must return the string "°C" if the temperature unit is Celsius or "°F" if the temperature unit is Fahrenheit.

celsiusUnit := Celsius
fahrenheitUnit := Fahrenheit

celsiusUnit.String()
// => °C
fahrenheitUnit.String()
// => °F
fmt.Sprint(celsiusUnit)
// Output: °C

Stuck? Reveal Hints
Opens in a modal
Temperature values consist of an integer and a temperature unit. They should be formatted as in the examples below.

For that to happen, make the Temperature type implement the Stringer interface by adding a String method to it. This method should return a string with the numeric value for the temperature and the temperature unit separated by a space: <temperature> <unit>:

celsiusTemp := Temperature{
    degree: 21,
    unit: Celsius,
}
celsiusTemp.String()
// => 21 °C
fmt.Sprint(celsiusTemp)
// Output: 21 °C

fahrenheitTemp := Temperature{
    degree: 75,
    unit: Fahrenheit,
}
fahrenheitTemp.String()
// => 75 °F
fmt.Sprint(fahrenheitTemp) 
// Output: 75 °F

Stuck? Reveal Hints
Opens in a modal
After lengthy discussions, the team has agreed that the unit of wind speed will be either KmPerHour or MilesPerHour. Values should be formatted as the examples below.

For that to happen, make the SpeedUnit type implement the Stringer interface by adding a String method to it. This method must return the string "km/h" if the speed unit is kilometers per hour or "mph" if the speed unit is miles per hour:

mphUnit := MilesPerHour
mphUnit.String()
// => mph
fmt.Sprint(mphUnit)
// Output: mph

kmhUnit := KmPerHour
kmhUnit.String()
// => km/h
fmt.Sprint(kmhUnit)
// Output: km/h

Stuck? Reveal Hints
Opens in a modal
Wind speed values consist of an integer and a speed unit. They should be formatted as in the example below.

For that to happen, make the Speed type implement the Stringer interface by adding a String method to it. This method should return a string with the numeric value for the speed and the speed unit separated by a space: <speed> <unit>:

windSpeedNow := Speed{
    magnitude: 18,
    unit: KmPerHour,
}
windSpeedNow.String(windSpeedNow)
// => 18 km/h
fmt.Sprintf(windSpeedNow)
// Output: 18 km/h

windSpeedYesterday := Speed{
    magnitude: 22,
    unit: MilesPerHour,
}
windSpeedYesterday.String(windSpeedYesterday)
// => 22 mph
fmt.Sprint(windSpeedYesterday)
// Output: 22 mph

Stuck? Reveal Hints
Opens in a modal
Meteorological data specifies location, temperature, wind direction, wind speed and humidity. It should be formatted as in the example below:

For that to happen, make the MeteorologyData type implement the Stringer interface by adding a String method to it. This method should return the meteorology data in the following format:

<location>: <temperature>, Wind <wind_direction> at <wind_speed>, <humidity>% Humidity
sfData := MeteorologyData{
    location: "San Francisco",
    temperature: Temperature{
        degree: 57,
        unit: Fahrenheit
    },
    windDirection: "NW",
    windSpeed: Speed{
        magnitude: 19,
        unit: MilesPerHour
    },
    humidity: 60
}

sfData.String()
// => San Francisco: 57 °F, Wind NW at 19 mph, 60% Humidity
fmt.Sprint(sfData) 
// Output: San Francisco: 57 °F, Wind NW at 19 mph, 60% Humidity