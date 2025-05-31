package expenses

import "errors"

// Record represents an expense record.
type Record struct {
	Day      int
	Amount   float64
	Category string
}

// DaysPeriod represents a period of days for expenses.
type DaysPeriod struct {
	From int
	To   int
}

// Filter returns the records for which the predicate function returns true.
func Filter(in []Record, predicate func(Record) bool) []Record {
	var res = []Record{}
	for _, v := range in {
		if predicate(v) {
			res = append(res, v)
		}
	}
	return res
}

// ByDaysPeriod returns predicate function that returns true when
// the day of the record is inside the period of day and false otherwise.
func ByDaysPeriod(p DaysPeriod) func(Record) bool {

	inner := func(r Record) bool {
		return r.Day >= p.From && r.Day <= p.To
	}
	return inner
}

// ByCategory returns predicate function that returns true when
// the category of the record is the same as the provided category
// and false otherwise.
func ByCategory(c string) func(Record) bool {

	inner := func(r Record) bool {
		return r.Category == c
	}
	return inner
}

// TotalByPeriod returns total amount of expenses for records
// inside the period p.
func TotalByPeriod(in []Record, p DaysPeriod) float64 {

	var vals = Filter(in, ByDaysPeriod(p))
	var res = 0.0
	for _, v := range vals {
		res += v.Amount
	}
	return res
}

// CategoryExpenses returns total amount of expenses for records
// in category c that are also inside the period p.
// An error must be returned only if there are no records in the list that belong
// to the given category, regardless of period of time.
func CategoryExpenses(in []Record, p DaysPeriod, c string) (float64, error) {

	categoryExists := false
	for _, record := range in {
		if record.Category == c {
			categoryExists = true
			break
		}
	}
	if !categoryExists {
		return 0, errors.New("Unknown category " + c)
	}
	categoryRecords := Filter(in, ByCategory(c))
	periodAndCategoryRecords := Filter(categoryRecords, ByDaysPeriod(p))

	var total float64 = 0
	for _, record := range periodAndCategoryRecords {
		total += record.Amount
	}
	return total, nil

}
