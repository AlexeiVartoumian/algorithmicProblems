package models

// getroute on teacher gives either one teacher or all
// json tags are important posting and getting and tell the encoder/decoder what to expect for the key
type Teacher struct {
	ID        int    `json:"id,omitempty"`
	FirstName string `json:"first_name,omitempty"`
	LastName  string `json:"last_name,omitempty"`
	Class     string `json:"class,omitempty"`
	Subject   string `json:"subject,omitempty"`
}
