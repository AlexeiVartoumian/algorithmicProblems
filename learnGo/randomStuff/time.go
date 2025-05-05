package booking

import ("time" 
        "fmt" )

// Schedule returns a time.Time from a string containing a date.
func Schedule(date string) time.Time {

    //digit sensitive on input i.e if input "7/25/2019 13:45:00" then that month digit shuould be represented as 1 not 01
    layout := "1/02/2006 15:04:05"

    t , err :=  time.Parse(layout, date)

    if err != nil  {
        fmt.Println(err)
    }
    return t
    
}

// HasPassed returns whether a date has passed.
func HasPassed(date string) bool {
	
	layout := "January 2, 2006 15:04:05"
    t , err :=  time.Parse(layout, date)

    if err != nil  {
        fmt.Println(err)
    }
    //var timer = Schedule(t)

    return time.Now().After(t)
}

// IsAfternoonAppointment returns whether a time is in the afternoon.
func IsAfternoonAppointment(date string) bool {

    // if january 2 is defined as january 02 then will only parse single digits with leading zeroes.
    layout := "Monday, January 2, 2006 15:04:05"
    t,err := time.Parse(layout , date)

    if err != nil {
        fmt.Println(err)
    }
    return t.Hour() >= 12 && t.Hour() <18 
}

// Description returns a formatted string of the appointment time.
func Description(date string) string {

    layout := "1/2/2006 15:04:05"
    t, err := time.Parse(layout, date)
    if err != nil {
        fmt.Println(err)
    }
    outputlayout := "You have an appointment on Monday, January 2, 2006, at 15:04."
    var val = t.Format(outputlayout)
    return val
}

// AnniversaryDate returns a Time with this year's anniversary.
func AnniversaryDate() time.Time {

    var currentYear = time.Now().Year() 
    
    var timer =  time.Date(currentYear , time.September,int(15),int(0),int(0),int(0),int(0),time.UTC)

    return timer
    