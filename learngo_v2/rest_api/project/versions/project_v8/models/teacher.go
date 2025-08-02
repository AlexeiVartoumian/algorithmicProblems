package models

// getroute on teacher gives either one teacher or all
// json tags are important posting and getting and tell the encoder/decoder what to expect for the key
// omitempty -> field should be omitted from the JSON output if its value is the zero value of the type

// take note that if inserting values to a db then can also indluce the db tag as seen in uncommented out version
// there are librarires such as goorm and sqlx taht will read the tags and create the sql queries

// type Teacher struct {
// 	ID        int    `json:"id,omitempty"`
// 	FirstName string `json:"first_name,omitempty"`
// 	LastName  string `json:"last_name,omitempty"`
// 	Email     string `json:"email,omitempty"`
// 	Class     string `json:"class,omitempty"`
// 	Subject   string `json:"subject,omitempty"`
// }

type Teacher struct {
	ID        int    `json:"id,omitempty" db:"id,omitempty"`
	FirstName string `json:"first_name,omitempty" db:"first_name,omitempty"`
	LastName  string `json:"last_name,omitempty" db:"last_name,omitempty"`
	Email     string `json:"email,omitempty" db:"email,omitempty"`
	Class     string `json:"class,omitempty" db:"class,omitempty"`
	Subject   string `json:"subject,omitempty" db:"subject,omitempty"`
}
